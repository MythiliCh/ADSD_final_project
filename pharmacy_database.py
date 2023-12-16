import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('pharmacy.db')
cursor = connection.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT NOT NULL,
        disease TEXT NOT NULL
    )
''')

#
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


def get_patients(patient_id=None):
    if patient_id is not None:
        cursor.execute("SELECT * FROM patients WHERE patient_id=?", (patient_id,))
    else:
        cursor.execute("SELECT * FROM patients")

    rows = cursor.fetchall()
    patients = [{'patient_id': row[0], 'patient_name': row[1], 'disease': row[2]} for row in rows]
    return patients



def get_medicines():
    cursor.execute("SELECT * FROM medicines")
    rows = cursor.fetchall()
    medicines = [{'medicine_id': row[0], 'medicine_name': row[1]} for row in rows]
    return medicines

def get_patient_meds(patient_id):
    cursor.execute("SELECT medicine_id FROM patient_meds WHERE patient_id=?", (patient_id,))
    rows = cursor.fetchall()
    medicine_ids = [row[0] for row in rows]
    
    medicines = []
    for medicine_id in medicine_ids:
        cursor.execute("SELECT * FROM medicines WHERE medicine_id=?", (medicine_id,))
        row = cursor.fetchone()
        medicines.append({'medicine_id': row[0], 'medicine_name': row[1]})
    
    return medicines

def add_patient(patient_name, disease):
    cursor.execute("INSERT INTO patients (patient_name, disease) VALUES (?, ?)", (patient_name, disease))
    connection.commit()

def add_medicine(medicine_name):
    cursor.execute("INSERT INTO medicines (medicine_name) VALUES (?)", (medicine_name,))
    connection.commit()

def add_patient_med(patient_id, medicine_id):
    cursor.execute("INSERT INTO patient_meds (patient_id, medicine_id) VALUES (?, ?)", (patient_id, medicine_id))
    connection.commit()

def update_patient(patient_id, patient_name, disease):
    cursor.execute("UPDATE patients SET patient_name=?, disease=? WHERE patient_id=?", (patient_name, disease, patient_id))
    connection.commit()

def delete_patient(patient_id):
    cursor.execute("DELETE FROM patients WHERE patient_id=?", (patient_id,))
    connection.commit()
