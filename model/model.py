import pickle
def main():
	# import lda model from sotored_models/
	lda_model = pickle.load(open('model/stored_models/lda.pkl', 'rb'))
	# test a value
	print(lda_model.predict([[-69]]))
	val_set = [(-33,0),(-33,0),(-33,0),(-34,0),(-69,1),(-68,1),(-70,1),(67,1),(-72,2),(-73,2),(-73,2),(-72,2)]
	# calculate accuracy
	
if __name__ == '__main__':
	#print base path 
	import os
	print(os.getcwd())
	main()