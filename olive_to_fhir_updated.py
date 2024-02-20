import os
import json
from datetime import datetime, timedelta
import pandas as pd

# Assuming 'resources' module contains the 'Patient' and 'ObservationVisualAcuity' classes
from resources.observation import ObservationVisualAcuity
from resources.patient import Patient

# Define the bcva_to_logmar_linear function
def bcva_to_logmar_linear(bcva_score, max_logmar=2.0):
    bcva_score = max(0, min(100, bcva_score))
    logmar_value = max_logmar * (1 - bcva_score / 100)
    return logmar_value

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv('Flattened_Training_Data_With_Label.csv')

# PATIENTS
df_patient = df[["Patient_ID"]].drop_duplicates()
for index, row in df_patient.iterrows():
    patient = Patient(id=str(row['Patient_ID']))
    if not os.path.exists(os.path.join(BASE_DIR, "logs/patient")):
        os.makedirs(os.path.join(BASE_DIR, "logs/patient"))
    with open(os.path.join(BASE_DIR, "logs/patient/") + "Patient_" + str(row['Patient_ID']) + ".json", "w") as f:
        json.dump(json.loads(patient.json()), f, indent=4)

# VISUAL ACUITY AS OBSERVATION
df_measurements = df[["Eye_ID", "Patient_ID", "Week", "BCVA", "CST", "Treatment_Label"]].drop_duplicates()
df_measurements['id'] = range(len(df_measurements))

# Convert BCVA to logMAR and add as a new column
df_measurements['logmar_VA'] = df_measurements['BCVA'].apply(bcva_to_logmar_linear)

df_measurements['bodysite_code'] = df_measurements['Eye_ID'].apply(lambda x: '362503005' if x in (1, 3, 4, 9, 11, 12, 17, 19, 30) else '362502000')
df_measurements['bodysite_display'] = df_measurements['Eye_ID'].apply(lambda x: 'Entire Left eye' if x in (1, 3, 4, 9, 11, 12, 17, 19, 30) else 'Entire Right eye')

initial_date = datetime(2020, 1, 1)
df_measurements['effectiveDateTime'] = initial_date + pd.to_timedelta(df_measurements['Week'], unit='W')

for index, row in df_measurements.iterrows():
    observationBCVA = ObservationVisualAcuity(
        id=str(row['id']),
        patientid=str(row['Patient_ID']),
        snomed_code="419775003",
        snomed_display="LogMAR visual acuity",
        effectiveDateTime=row['effectiveDateTime'],
        value=str(row['logmar_VA']),
        unit='logMAR',  # Updated to 'logMAR' to reflect the new value
        bodysite_code=row['bodysite_code'],
        bodysite_display=row['bodysite_display'],
        method_code="400913005",
        method_display="ETDRS chart"
    )

    if not os.path.exists(os.path.join(BASE_DIR, "logs/observation")):
        os.makedirs(os.path.join(BASE_DIR, "logs/observation"))
    with open(os.path.join(BASE_DIR, "logs/observation/") + "ObservationlogMAR" + str(row['id']) + ".json", "w") as f:
        json.dump(json.loads(observationBCVA.json()), f, indent=4)
