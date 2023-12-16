<!DOCTYPE html>
<html>
<head>
    <title>Patients</title>
</head>
<body>
    <h1>Patients</h1>

    <form action="/patients" method="get">
        Search: <input type="text" name="search" value="{{search_term}}">
        <input type="submit" value="Search">
    </form>

    <hr></hr>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Patient Name</th>
            <th>Disease</th>
            <th>Update Here</th>
            <th>Delete Here</th>
        </tr>
        % for item in patients:
            <tr>
                <td>{{str(item['patient_id'])}}</td>
                <td>{{item['patient_name']}}</td>
                <td>{{item['disease']}}</td>
                <td><a href="/patients/update/{{str(item['patient_id'])}}">update</a></td>
                <td><a href="/patients/delete/{{str(item['patient_id'])}}">delete</a></td>
            </tr>
        % end
    </table>
    <hr/>
<a href="add_patient">Add new Patient</a>
<hr/>
</body>
</html>
