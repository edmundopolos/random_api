from flask import Flask, request,  Blueprint
from datetime import *
from flask_restful import Resource, Api 
from uuid import *

app = Flask(__name__)
api = Api(app)
blueprint = Blueprint('RUUID', __name__)

class UniqueStamp(Resource):
    def get(self):
        a = datetime.now().strftime('%Y-%m-%d %H:%I:%m')
        return {a:str(uuid1())}

api.add_resource(UniqueStamp, '/')


if __name__ == '__main__':
  app.run(host='0.0.0.0',port='5000',debug=True)