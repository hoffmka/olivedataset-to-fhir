import json
import os
import json
from datetime import datetime, timedelta

import sys
 
# setting path
parent_directory = os.path.abspath('../..')
sys.path.append(parent_directory)

import pandas as pd
from resources.observation import ObservationVisualAcuity
from resources.patient import Patient

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv('src/Flattened_Training_Data_With_Label.csv')

###############################
# PATIENTS
###############################
df_patient = df[["Patient_ID"]].drop_duplicates()
# Create fhir resources "Patient" for each row in dataframe
for index, row in df_patient.iterrows():
    patient = Patient(id=str(row['Patient_ID']))
    # WRITE TO FILE
    # create folder "output/patient" if not exists
    if not os.path.exists(os.path.join(BASE_DIR, "output/patient")):
        os.makedirs(os.path.join(BASE_DIR, "output/patient"))
    with open(
        os.path.join(BASE_DIR, "output/patient/") + "Patient_" + str(row['Patient_ID']) + ".json", "w",
    ) as f:
        json.dump(json.loads(patient.json()), f, indent=4)


##############################
# VISUAl ACUITY AS OBSERVATION
##############################
df_measurements = df[["Eye_ID", "Patient_ID", "Week", "BCVA", "CST", "Treatment_Label"]].drop_duplicates()
df_measurements['id'] = range(len(df_measurements))

# set snomed code for right and left eye --> https://www.findacode.com/snomed/244486005--entire-eye.
df_measurements['bodysite_code'] = df_measurements['Eye_ID'].apply(lambda x: '362503005' if x in (1, 3, 4, 9, 11, 12, 17, 19, 30) else '362502000')
df_measurements['bodysite_display'] = df_measurements['Eye_ID'].apply(lambda x: 'Entire Left eye' if x in (1, 3, 4, 9, 11, 12, 17, 19, 30) else 'Entire Right eye')

# constructing effectiveDateTime based on an initial_date and the week number
initial_date = datetime(2020, 1, 1)
df_measurements['effectiveDateTime'] = initial_date + pd.to_timedelta(df['Week'], unit='W')

for index, row in df_measurements.iterrows():
    observationVisualAcuity = ObservationVisualAcuity(
        id=str(row['id']),
        patientid=str(row['Patient_ID']),
        # code_code and code_display from snomed, belong together, cf. valueset: https://build.fhir.org/ig/HL7/fhir-eyecare-ig/ValueSet-observation-visual-acuity.html
        code_code="419775003",
        code_display="Best corrected visual acuity",
        effectiveDateTime=row['effectiveDateTime'], # constructed effectiveDateTime
        value=str(row['BCVA']),
        unit='', # Todo: Ask Gabriel about the unit (Empty is okay? Maybe "%"?) 
        # Todo: Create a BodyStructure resource and refer to bodysite 
        bodysite_code=row['bodysite_code'],
        bodysite_display=row['bodysite_display'],
        # method_code and method_display from snomed, cf. valueset https://build.fhir.org/ig/HL7/fhir-eyecare-ig/ValueSet-observation-visual-acuity-methods.html
        method_code="400914004", 
        method_display="ETDRS visual acuity chart"
    )

    # WRITE TO FILE
    # create folder "output/observation" if not exists
    if not os.path.exists(os.path.join(BASE_DIR, "output/observation")):
        os.makedirs(os.path.join(BASE_DIR, "output/observation"))
    with open(
        os.path.join(BASE_DIR, "output/observation/") + "ObservationBCVA" + str(row['id']) + ".json", "w",
    ) as f:
        json.dump(json.loads(observationVisualAcuity.json()), f, indent=4)
