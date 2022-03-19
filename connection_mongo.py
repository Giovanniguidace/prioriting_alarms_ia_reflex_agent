import pymongo

def connMongoDB():
    connMongoDB = pymongo.MongoClient("mongodb://localhost:27017/")
    return connMongoDB

def connRules():
    application_connection = pymongo.MongoClient("mongodb://localhost:27017/")
    get_rules = list(application_connection["ia_priority_alarms"]["rules"].find({}))
    return get_rules


def connAlarms():
    application_connection = pymongo.MongoClient("mongodb://localhost:27017/")
    get_metrics_machine_resources = list(application_connection["metrics"]["machine_resources"].find({}))
    return get_metrics_machine_resources

