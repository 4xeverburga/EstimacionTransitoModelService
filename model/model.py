import pickle
import json

def clf_model(signal_strength):
	"""classify the signal strength into a region"""
	# import lda model from sotored_models/
	lda_model = pickle.load(open('model/stored_models/lda.pkl', 'rb'))
	# return the region
	return lda_model.predict([[signal_strength]])[0]

def main():
	# import lda model from sotored_models/
	lda_model = pickle.load(open('model/stored_models/lda.pkl', 'rb'))
	# test a value
	print(lda_model.predict([[-33]]))
	val_set = [(-33,0),(-33,0),(-33,0),(-34,0),(-69,1),(-68,1),(-70,1),(67,1),(-72,2),(-73,2),(-73,2),(-72,2)]
	# calculate accuracy
	accuracy = 0
	for val in val_set:
		print(lda_model.predict([[val[0]]]))
		if int(lda_model.predict([[val[0]]])[0]) == val[1]:
			accuracy += 1
	print('Accuracy: ', accuracy/len(val_set))

 
def load_separator(json_input):
	"""separate the messagges into loads with the same mac""" 
	loads = [[]] # a list of jsons with the same mac
	# the json is a list of dictionaries

	# the first dictionary is the first message
	loads[0].append(json_input[0])
	# if the mac is the same as the last one, add it to the last load
	# if not, create a new load
	for i in range(1,len(json_input)):
		if json_input[i]['mac_origen'] == loads[-1][-1]['mac_origen']:
			loads[-1].append(json_input[i])
		else:
			loads.append([json_input[i]])

	return loads


def load_separator_test():
	#load json from feria2023.mensajes.json
	json_input = json.load(open('model/feria2023.mensajes.json', 'r'))
	#delete the dicts that don't have a mac_origen
	json_input = [x for x in json_input if 'mac_origen' in x]
	# json_input is a list of dictionaries. I want to sort them by mac_origen first
	# then I want to separate them into loads
	sorted(json_input, key=lambda k: k['mac_origen'])
	loads = load_separator(json_input)
	# print the number of loads
	print("number of different macs: ",len(loads))
	# classify the loads
	res = classifier(loads)
	# print the result
	print(res)

def classifier(loads):
	"""
	classify the loads into a number of people
	to simplify the problem, we will assign a region to a unique vertex and the other way around
	the output is a dict with the id of the edge and the number of people
	"""
	# assuming the load is from a 2 minute period we will only use the average of the last or first 3 messages
	# the average will be the input of the model
	avgs = [] 
	for load in loads:
		avg = 0
		# for i in range 3 or the max number of messages in the load
		for i in range(min(3,len(load))):
			avg += load[i]['fuerza_senial']
		avg /= min(3,len(load))
		avgs.append(avg)
	
	map_regions = { # these are arbitrary assignments
		'0': '656d780d721bc5cd177bd974',
		'1': '656d796d721bc5cd177bd979',
		'2': '656d7bab721bc5cd177bd97d'		
		}
	
	outp = [] # list of dict with the id of the edge and the number of people

	CORRECTION_FACTOR = 1/0.8 # people don't use wifi networks all the time
	region_count = {'0': 0, '1': 0, '2': 0}
	for avg in avgs:
		region_count[str(clf_model(avg))] += 1
	for region in region_count:
		outp.append({'id': map_regions[region], 'num_people': region_count[region]*CORRECTION_FACTOR})
	return outp

if __name__ == '__main__':
	#print base path 
	import os
	print(os.getcwd())
	load_separator_test()