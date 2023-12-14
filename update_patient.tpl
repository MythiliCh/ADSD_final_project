<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Patient Details</title>
</head>
<body>
    <h1>Update Patient Details</h1>

    <form action="/patients/update/{{ patient.patient_id }}" method="post">

        <label for="patient_name">Patient Name:</label>
        <input type="text" id="patient_name" name="patient_name" value="{{ patient.patient_name }}" required>

        <label for="disease">Disease:</label>
        <input type="text" id="disease" name="disease" value="{{ patient.disease }}" required>

        <button type="submit">Update Patient</button>
    </form>

    <a href="/patients">Back to Patients</a>
</body>
</html>
