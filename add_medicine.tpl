<!DOCTYPE html>
<html>
<head>
    <title>Add Medicine</title>
</head>
<body>
    <h1>Add Medicine</h1>
    <form action="/add_medicine" method="post">
        <label for="medicine_name">Medicine Name:</label>
        <input type="text" id="medicine_name" name="medicine_name" required><br>

        <input type="submit" value="Add Medicine">
    </form>
    <hr/>
    <a href="/medicines">Back to Medicines</a>
</body>
</html>
