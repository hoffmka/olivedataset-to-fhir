[Back to README](../README.md)

## OLIVE dataset example resources

### Example Patient:

```json
{
    "resourceType": "Patient",
    "id": "201"
}
```

### Example BCVA

```json
{
    "resourceType": "Observation",
    "id": "0",
    "status": "final",
    "category": [
        {
            "coding": [
                {
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "exam",
                    "display": "Exam"
                }
            ]
        }
    ],
    "code": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "419775003",
                "display": "Best corrected visual acuity"
            }
        ]
    },
    "subject": {
        "reference": "Patient/201"
    },
    "effectiveDateTime": "2020-01-08T00:00:00",
    "valueQuantity": {
        "value": "61.0",
        "unit": ""
    },
    "bodySite": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "362503005",
                "display": "Entire Left eye"
            }
        ]
    },
    "method": {
        "coding": [
            {
                "system": "http://snomed.info/sct",
                "code": "400914004",
                "display": "ETDRS visual acuity chart"
            }
        ]
    }
}
```