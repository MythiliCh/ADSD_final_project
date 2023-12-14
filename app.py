from bottle import route, post, run, template, redirect, request
import pharmacy_database

@route("/")
def get_index():
    return template('index')

@route("/patients")
def get_patients():
    items = pharmacy_database.get_patients()
    search_term = request.forms.get('search_term')
    return template('patients', patients=items, search_term=search_term)

@route("/patient_meds/<patient_id:int>")
def get_patient_meds(patient_id):
    items = pharmacy_database.get_patient_meds(patient_id)
    return template('patient_meds', patient_id=patient_id, patient_meds=items)

@route("/add_patient")
def add_patient():
    return template('add_patient')

@post("/add_patient")
def post_add_patient():
    patient_name = request.forms.get("patient_name")
    disease = request.forms.get("disease")
    pharmacy_database.add_patient(patient_name, disease)
    redirect("/patients")

@route("/medicines")
def get_medicines():
    items = pharmacy_database.get_medicines()
    search_term = request.forms.get('search_term')
    return template('medicines', medicines=items, search_term=search_term)



@route("/add_patient_med")
def add_patient_med():
    patients = pharmacy_database.get_patients()
    medicines = pharmacy_database.get_medicines()
    return template('add_patient_med', patients=patients, medicines=medicines)

@post("/add_patient_med")
def post_add_patient_med():
    patient_id = request.forms.get("patient_id")
    medicine_id = request.forms.get("medicine_id")
    pharmacy_database.add_patient_med(patient_id, medicine_id)
    redirect(f"/patient_meds/{patient_id}")

@route("/patients/update/<patient_id>")
def get_update_patient(patient_id):
    items = pharmacy_database.get_patients(patient_id)
    return template("update_patient.tpl", item=items[0])

@post("/patients/update/<patient_id>")
def post_update_patient(patient_id):
    patient_name = request.forms.get("patient_name")
    disease = request.forms.get("disease")
    pharmacy_database.update_patient(patient_id, patient_name, disease)
    redirect("/patients")

@route("/patients/delete/<patient_id>")
def get_delete_patient(patient_id):
    pharmacy_database.delete_patient(patient_id)
    redirect("/patients")

run(host='localhost', port=8090)


# @post("/add_medicine")
# def post_add_medicine():
#     medicine_name = request.forms.get("medicine_name")
#     pharmacy_database.add_medicine(medicine_name)
#     redirect("/medicines")
#@route("/add_medicine")
# def add_medicine():
#     return template('add_medicine')


