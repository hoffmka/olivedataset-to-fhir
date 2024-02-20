# olivedataset-to-fhir
## BCVA to logMAR
### Source
Paper - https://arxiv.org/pdf/2209.11195.pdf    

ETDRS best-corrected
visual acuity (BCVA) is a visual function assessment performed by certified examiners where a
standard vision chart is placed 4 meters away from the patient. The patient is instructed to read the
chart from left to right, from top to bottom until the subject completes 6 rows of letters or the subject
is unable to read any more letters. The examiner marks how many letters were correctly identified by
the patient. 
#### ETDRS and Snellen chart relation 
A Snellen score of 6/6 (20/20), indicating that an observer can resolve details as small as 1 minute of visual angle, corresponds to a LogMAR of 0 (since the base-10 logarithm of 1 is 0); 6 meters log value is 0.2 and var is 90, max log value is 1.0
based on this I created a function that is available in olive_to_fhir_updated.py, and in logs folders sample JSON files are available


