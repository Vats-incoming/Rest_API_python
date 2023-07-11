from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

class Users(Resource):
   
    def get(self):
        data = pd.read_csv('users.csv')
        data = jsonify(data)
        return {'data' : data}, 200
    

    def post(self):
        parser = reqparse.RequestParser()  
        parser.add_argument('userId', required=True) 
        parser.add_argument('name', required=True)
        parser.add_argument('city', required=True)
        
        args = parser.parse_args()  
        new_data = pd.DataFrame({
            'userId': args['userId'],
            'name': args['name'],
            'city': args['city'],
            'locations': [[]]
        })
        
        data = pd.read_csv('users.csv') 
        data = data.append(new_data, ignore_index=True)
        data.to_csv('users.csv', index=False)
        return {'data': data.to_dict()}, 200  



app = Flask(__name__)
api = Api(app)
api.add_resource(Users, '/users')
if (__name__ == '__main__'):
    app.run()