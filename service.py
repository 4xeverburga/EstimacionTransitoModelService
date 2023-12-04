import model.model as model
import flask
from flask import request
import os
import json


host = os.environ.get('HOST')
port = os.environ.get('PORT')


app = flask.Flask(__name__)

# a get route with name estimationService
# this route will be used for getting the estimation
@app.route('/estimationService', methods=['POST'])
def estimationService():
	"""
	input de ejemplo: 
	{
		"aristas": [
			{"id": "507f1f77bcf86cd799439011",
				"nodo1_id": "507f1f77bcf86cd799439012",
				"latitud1": 1.1,
				"longitud1": 1.1,
				"nodo2_id": "507f1f77bcf86cd799439013", 
				"latitud2": 1.1,
				"longitud2": 1.1,
			}
		],
		"mensajes": [
			{"id": "507f1f77bcf86cd799439014",
			"mac_origen": "aa:aa:aa:aa:aa:aa",
			"fuerza": "-50"
			},
			{"id": "507f1f77bcf86cd799439015",
			"mac_origen": "aa:aa:aa:aa:aa:aa",
			"fuerza": -52
			},
			{"id": "507f1f77bcf86cd799439016",
			"mac_origen": "aa:aa:aa:aa:aa:aa",
			"fuerza": -54
			},
			{"id": "507f1f77bcf86cd799439017",
			"mac_origen": "aa:aa:aa:aa:aa:ab",
			"fuerza": -30
			}
		]
	}
	output de ejemplo:
	{
		"aristas": [
			{"id": "507f1f77bcf86cd799439011",
			"personas": 2}
		]
	}

	Consideraciones:
	- De momento solo la id de las aristas es necesaria
	- La id de los mensajes no es necesaria por ahora y puede ser no enviada

	"""
	post_data = request.get_json()
	print(post_data)
	model.main()
	return flask.jsonify({'status': 'success'})

	

# deploy the service
app.run(host="0.0.0.0", port=5000)
