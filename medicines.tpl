

<!DOCTYPE html>
<html>
<head>
    <title>Medicines</title>
</head>
<body>
    <h1>Medicines</h1>

    <form action="/medicines" method="get">
        Search: <input type="text" name="search" value="{{search_term}}">
        <input type="submit" value="Search">
    </form>

    <hr></hr>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Medicine Name</th>
        </tr>
        % for item in medicines:
            <tr>
                <td>{{str(item['medicine_id'])}}</td>
                <td>{{item['medicine_name']}}</td>
            </tr>
        % end
    </table>
    <hr/>
<a href="add_medicine">Add new Medicine</a>
<hr/>
</body>
</html>

