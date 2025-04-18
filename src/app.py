# app.py
from flask import Flask, jsonify
from flask_restful import Resource, Api
import datetime
import os
import platform

app = Flask(__name__)
api = Api(app)

class HealthCheck(Resource):
    def get(self):
        return {
            'status': 'healthy',
            'version': '1.0.1',
            'environment': os.getenv('FLASK_ENV', 'development')
        }

class ServerInfo(Resource):
    def get(self):
        return {
            'python_version': platform.python_version(),
            'hostname': platform.node(),
            'system': platform.system()
        }

class CurrentTime(Resource):
    def get(self):
        return {
            'utc_time': datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(),
            'local_time': datetime.datetime.now().astimezone().isoformat()
        }
class Details(Resource):
    def get(self):
        return {
            'app_name': 'Python App with ArgoCD',
            'developer': 'Asad Hanif',
            'serving_from': 'Kubernetes',
            'team_members': 'Haroon, Saqib',
            'other_members': 'Salman, Hamza, Safo',
        }

api.add_resource(HealthCheck, '/health')
api.add_resource(ServerInfo, '/info')
api.add_resource(CurrentTime, '/time')
api.add_resource(Details, '/api/v1/details')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.getenv('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)