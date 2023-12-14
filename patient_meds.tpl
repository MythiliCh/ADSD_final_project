<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Medicines</title>
</head>
<body>
    <h1>Medicines</h1>

        % for patient_med in patient_meds:
            <h2>{{patient_med.patient_id}} - {{ patient_med.disease }} - {{ patient_med.medicine_name }}</h2>
        % end

    
</body>
</html>
