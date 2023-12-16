<!DOCTYPE html>
<html>
<head>
    <title>Add Patient</title>
</head>
<body>
    <h1>Add Patient</h1>
    <form action="/add_patient" method="post">
        <label for="patient_name">Patient Name:</label>
        <input type="text" id="patient_name" name="patient_name" required><br>

        <label for="disease">Disease:</label>
        <input type="text" id="disease" name="disease" required><br>

        <input type="submit" value="Add Patient">
    </form>
    <hr/>
    <a href="/patients">Back to Patients</a>
</body>
</html>
