from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.observation import Observation
from fhir.resources.quantity import Quantity
from fhir.resources.reference import Reference

class ObservationVisualAcuity(Observation):
    def __init__(self, id, patientid, snomed_code, snomed_display, effectiveDateTime, value, unit, bodysite_code, bodysite_display, method_code, method_display):
        super().__init__(
            id=id,
            status="final",
            category=[CodeableConcept.construct(
                coding=[
                    Coding.construct(
                        system="http://terminology.hl7.org/CodeSystem/observation-category",
                        code="exam",
                        display="Exam"
                    )
                ]
            )],
            code=CodeableConcept.construct(
                coding=[
                    Coding.construct(
                        system="http://snomed.info/sct",
                        code=snomed_code,
                        display=snomed_display
                    )
                ]
            ),
            subject = Reference.construct(reference="Patient/"+patientid),
            effectiveDateTime = effectiveDateTime,
            valueQuantity = Quantity.construct(
                value = value,
                unit = unit,
            ),
            method=CodeableConcept.construct(
                coding=[Coding.construct(
                    system="http://snomed.info/sct",
                    code=method_code,
                    display=method_display
                )]
            ),
            bodySite=CodeableConcept.construct(
                coding=[
                    Coding.construct(
                        system="http://snomed.info/sct",
                        code=bodysite_code,
                        display=bodysite_display
                    )
                ]
            )
        )
