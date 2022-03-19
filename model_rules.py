
import connection_mongo

rules = [
{"percept_name": "CPU", "percept_ref": "90", "percept_environment": "PROD", "priority": "P1"},
    {"percept_name": "CPU", "percept_ref": "90", "percept_environment": "DEV", "priority": "P3"},
{"percept_name": "RAM", "percept_ref": "90", "percept_environment": "PROD", "priority": "P1"},
{"percept_name": "RAM", "percept_ref": "90", "percept_environment": "DEV", "priority": "P3"},
{"percept_name": "DISK", "percept_ref": "90", "percept_environment": "PROD", "priority": "P1"},
{"percept_name": "DISK", "percept_ref": "90", "percept_environment": "DEV", "priority": "P3"}
         ]

def insertRules():
    db = connection_mongo.connMongoDB()["ia_priority_alarms"]
    col = db["rules"]
    for rule in rules:
        col.insert_one(rule)

    return "Insert OK"

#EXECUTION
insertRules()