import model.model as model
import flask
import os
import json


host = os.environ.get('HOST')
port = os.environ.get('PORT')


app = flask.Flask(__name__)

# a get route with name estimationService
# this route will be used for getting the estimation
@app.route('/estimationService', methods=['GET'])
def estimationService():
	return model.main()

	

# deploy the service
app.run(host=host, port=port)
