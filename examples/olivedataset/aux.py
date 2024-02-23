# Define the bcva_to_logmar_linear function
# if it is required for subsequent conversion in the application.
# It is not recommended to convert the value before mapping to fhir.
def bcva_to_logmar_linear(bcva_score, max_logmar=1.0):
    bcva_score = max(0, min(100, bcva_score))
    logmar_value = max_logmar * (1 - bcva_score / 100)
    return logmar_value