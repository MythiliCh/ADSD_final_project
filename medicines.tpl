<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medicines</title>
</head>
<body>
    <h1>Medicines</h1>

    <form action="/medicines" method="get">
        <input type="text" name="search_term" placeholder="Search Medicines">
        <button type="submit">Search</button>
    </form>

    <table border="1">
    <tr>
    <th>ID</th>
    <th>Patient Name</th>
    <th>Disease</th>
    <th>Prescribed_medicine</th>
    </tr>
    % for patient in patients:
    <tr>
    <td>{{str(patient.patient_id)}}</td>
    <td>{{str(patient.patient_name)}}</td>
    <td>{{str(patient.disease)}}</td>>
    <td><a href="/patient_med/{{str(patient.patient_id)}}">Click for your Medicine</a></td>
    </tr>


</body>
</html>
