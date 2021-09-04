from flask import Flask, jsonify,request
from flask_restx import Resource
from model import DataHandling
from helper import *

class_object = DataHandling()

class RecordHandling(Resource):
    
    def get(self):
        #try:
            column_name = request.get_json()
            
            data_histogram = class_object.histogram(column_name['column name'])
            return getCustomResponse(success=True, message="OK, Returning data from get method", data=data_histogram, status_code=200)

        #except:
            return getCustomResponse(success=False, message="Bad Request, Some error has occured while returning data from get method", data=None, status_code=400)
