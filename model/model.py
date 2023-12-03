import pickle
def main():
	# import lda model from sotored_models/
	lda_model = pickle.load(open('model/stored_models/lda.pkl', 'rb'))
	# test a value
	print(lda_model.predict([[-69]]))
if __name__ == '__main__':
	#print base path 
	import os
	print(os.getcwd())
	main()