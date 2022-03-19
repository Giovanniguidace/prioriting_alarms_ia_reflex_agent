import connection_mongo
machine_resources_example = [{
    "machine_name": 'PC23743',
    "metric_type": 'CPU',
    "metric_value": '40',
    "environment": 'DEV'
  },
  {
    "machine_name": 'PC33465',
    "metric_type": 'CPU',
    "metric_value": '95',
    "environment": 'PROD'
  },
  {
    "machine_name": 'PC33443',
    "metric_type": 'CPU',
    "metric_value": '91',
    "environment": 'DEV'
  },
  {
    "machine_name": 'PC43444',
    "metric_type": 'RAM',
    "metric_value": '93',
    "environment": 'PROD'
  },
  {
    "machine_name": 'PC34555',
    "metric_type": 'DISK',
    "metric_value": '80',
    "environment": 'DEV'
  }
]

def insertMetrics():
    db = connection_mongo.connMongoDB()["alarms"]
    col = db["machine_resources"]
    for metric in machine_resources_example:
        col.insert_one(metric)

    return "Insert OK"

#EXECUTION
insertMetrics()