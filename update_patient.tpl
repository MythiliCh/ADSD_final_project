<!DOCTYPE html>
<html>
<head>
    <title>Update Patient</title>
</head>
<body>
    <h1>Update Patient</h1>
    <form action="/patients/update/{{item['patient_id']}}" method="post">
        <label for="patient_name">Patient Name:</label>
        <input type="text" id="patient_name" name="patient_name" value="{{item['patient_name']}}" required><br>

        <label for="disease">Disease:</label>
        <input type="text" id="disease" name="disease" value="{{item['disease']}}" required><br>

        <input type="submit" value="Update Patient">
    </form>
    <hr/>
    <a href="/patients">Back to Patients</a>
</body>
</html>
