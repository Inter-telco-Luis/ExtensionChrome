from flask import Flask, request
from flask import Response
from flask_restful import Api, Resource, reqparse
from flask import jsonify
from flask_cors import CORS
from wand.image import Image
import cv2 as cv2
import numpy as np
import os
#from OpenSSL import SSL
from DB import fill_ef_segments
 
app = Flask(__name__)
api = Api(app)
CORS(app)
cors=CORS(app, resources={
    r"/*":{
        "origin":"*",
        'Access-Control-Allow-Origin': '*'
    }
})


'''
EJEMPLO DE PETICION
curl -d "ef=/home/pdi/Documents/React/OCR/ocr-it/eeff_100/900327563 EEFF IFRS.tif" -X POST http://localhost:1232/path
'''

# 400 Bad Request   
r_400 = Response("Peticion invalida.", status=400)

# 500 Internal Server Error
r_500 = Response("Error interno del servidor", status=500)


#context = SSL.Context(SSL.SSLv3_METHOD)
#context = SSL.Context(SSL.TLSv1_2_METHOD)
#context.use_certificate('cert.pem')
#context.use_privatekey('key.pem')


class User(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("datos")
        args = parser.parse_args()
        
        print('\nPARAMETROS ENTRADA:')
        for key,value in args.items():
            parameters=['','','','','','','','','','','','']
            parameters=value.split(",")
        
        fill_ef_segments(parameters)
            #print(key + ':', value)
            #for item in value:
             #   print(item)
                #
                #
                #
            #
            #
            #
        return value
            

api.add_resource(User, "/")

app.run(debug=True, port=1233, host='0.0.0.0') #pp.run(ssl_context=context,debug=True, port=1233, host='0.0.0.0')

