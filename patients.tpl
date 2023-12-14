<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patients</title>
</head>
<body>
    <h1>Patients</h1>

    <form action="/patients" method="get">
        <input type="text" name="search_term" placeholder="Search Patients">
        <button type="submit">Search</button>
    </form>
    <table border="1">
    <tr>
    <th>ID</th>
    <th>Patient Name</th>
    <th>Disease</th>
    <th>Update Here</th>
    <th>Delete Here</th>
    </tr>
    % for patient in patients:
    <tr>
    <td>{{str(patient.patient_id)}}</td>
    <td>{{str(patient.patient_name)}}</td>
    <td>{{str(patient.disease)}}</td>>
    <td><a href="/patient/update/{{str(patient.patient_id)}}">update</a></td>
    <td><a href="/patient/delete/{{str(patient.patient_id)}}">delete</a></td>
    </tr>
    % end
    </table>
    
    <a href="/patients/add">Add Patient</a>
</body>
</html>

