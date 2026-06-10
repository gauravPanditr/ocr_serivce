INSURANCE_PROMPT = """
Extract and return JSON:

{
  "policyNumber":"",
  "ownerName":"",
  "vehicleNumber":"",
  "insuranceValue":"",
  "policyStartDate":"",
  "policyEndDate":""
}
"""

RC_PROMPT = """
Extract and return JSON:

{
  "vehicleNumber":"",
  "ownerName":"",
  "engineNumber":"",
  "chassisNumber":"",
  "vehicleModel":""
}
"""

FIR_PROMPT = """
Extract and return JSON:

{
  "firNumber":"",
  "incidentDate":"",
  "incidentLocation":"",
  "vehicleNumber":""
}
"""

REPAIR_BILL_PROMPT = """
Extract and return JSON:

{
  "billNumber":"",
  "garageName":"",
  "repairAmount":"",
  "billDate":""
}
"""