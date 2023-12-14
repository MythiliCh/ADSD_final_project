<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Medicine to Patient</title>
</head>
<body>
    <h1>Add Medicine to Patient</h1>

    <form action="/patient_meds/add" method="post">
        <input type="hidden" name="patient_id" value="{{ patient_id }}">
        <label for="medicine_id">Select Medicine:</label>
        <select name="medicine_id" id="medicine_id">
            % for medicine in medicines:
                <option value="{{ medicine.medicine_id }}">{{ medicine.medicine_name }}</option>
            % end
        </select>
        <button type="submit">Add Medicine</button>
    </form>

    <a href="/patient_meds/{{ patient_id }}">Back to Patient Medicines</a>
</body>
</html>
