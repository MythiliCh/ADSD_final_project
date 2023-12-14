# pharmacy_database.py

import sqlite3
from bottle import Bottle, route, run, template, request, redirect

connection = sqlite3.connect("pharmacy.db")

app = Bottle()

@app.route('/patients')
def get_patients():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    patients = [{'patient_id': row[0], 'patient_name': row[1], 'disease': row[2]} for row in rows]
    print(patients)
    return template('patients', patients=patients)

@app.route('/medicines')
def get_medicines():
    cursor = connection.cursor()
    search_term = request.query.get('search', '').strip()
    
    if search_term:
        rows = cursor.execute("SELECT * FROM medicines WHERE medicine_name LIKE ?", (f"%{search_term}%",))
    else:
        rows = cursor.execute("SELECT * FROM medicines")

    medicines = [{'medicine_id': row[0], 'medicine_name': row[1]} for row in rows.fetchall()]
    return template('medicines', medicines=medicines, search_term=search_term)

@app.route('/patient_meds/<patient_id:int>')
def get_patient_meds(patient_id):
    cursor = connection.cursor()
    rows = cursor.execute("SELECT * FROM patient_meds WHERE patient_id = ?", (patient_id,))
    patient_meds = [{'patient_id': row[0], 'medicine_id': row[1]} for row in rows.fetchall()]
    return template('patient_meds', patient_id=patient_id, patient_meds=patient_meds)

@app.route('/add_patient')
def add_patient():
    return template('add_patient')



@app.route('/add_patient_med')
def add_patient_med():
    patients = connection.execute("SELECT * FROM patients").fetchall()
    medicines = connection.execute("SELECT * FROM medicines").fetchall()
    return template('add_patient_med', patients=patients, medicines=medicines)


# Initialize the database
def initialize_database():
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            disease TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicines (
            medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            medicine_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patient_meds (
            patient_id INTEGER,
            medicine_id INTEGER, 
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY (medicine_id) REFERENCES medicines(medicine_id)
        )
    ''')

    connection.commit()

if __name__ == "__main__":
    initialize_database()
    app.run(host='localhost', port=8080, debug=True)
