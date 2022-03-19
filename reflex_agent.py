


class ReflexAgent:

    def define_priority(connRules, connAlarms):
        for metric in list(connAlarms):
            for rule in list(connRules):
                if rule["percept_name"] == metric["metric_type"]:
                    if rule["percept_ref"] >= metric["metric_value"]:
                        if metric["environment"] == "PROD":
                            result = "This alert have the priority level: " + rule["priority"] + " ObjectID: " + str(metric["_id"])
                            print(result)
                        elif metric["environment"] == "DEV":
                            result = "This alert have the priority level: " + rule["priority"] + " ObjectID: " + str(metric["_id"])
                            print(result)



