"""
Extract S3 Records from AWS Event
EN
Given an AWS S3 event JSON, extract (bucket, key) for each record. 
Skip invalid or incomplete records.

ES
Dado un evento JSON de AWS S3, extrae (bucket, key) de cada registro.
Omite los registros inválidos o incompletos.

Example:
event = {"Records":[{"s3":{"bucket":{"name":"b"},"object":{"key":"f.txt"}}}]}
→ [("b","f.txt")]
"""
def s3_records(event):
    out = []
    for rec in event.get("Records", []):
        try:
            b = rec["s3"]["bucket"]["name"]
            k = rec["s3"]["object"]["key"]
            out.append((b, k))
        except (KeyError, TypeError):
            continue
    return out

event = {"Records":[{"s3":{"bucket":{"name":"bucket1"},"object":{"key":"file1.txt"}}}]}
print(s3_records(event))
