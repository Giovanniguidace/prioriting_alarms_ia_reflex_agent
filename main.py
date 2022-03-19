
from reflex_agent import ReflexAgent
import connection_mongo

if __name__ == '__main__':

    execute_agent = ReflexAgent.define_priority(connection_mongo.connRules(), connection_mongo.connAlarms())
