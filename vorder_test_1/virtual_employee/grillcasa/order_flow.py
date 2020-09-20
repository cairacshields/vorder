##
# 
#
#
# Demo order flow for fictional foodchain 'grillcasa'
# An order flow will take human responses to build out an order 
# 
# It's a converation. 
# Automated employee initiates the ordering process by saying the greeting. 
# After every automated sentence, we wait for a customer response. 
# That customer response then shapes what our next automated question will be. 
#
#
# ie:
# Begin with automated greeting
# take customer initial response ex: 'can i have a large coke?'
# find the requesting subject (using NLP, particularly parts of speech tagging)
# 
#
##

import pyttsx
import speech_recognition as sr
import spacy
import menu 

#initialize the virtual ordering employee :)
engine = pyttsx.init()
voices = engine.getProperty('voices')    
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#initialze the speech recognizer
recognizer = sr.Recognizer()

test_response = 'hi can i get two cheeseburgers' 

nlp = spacy.load("en_core_web_sm")
doc = nlp(u'hi can i get two cheeseburgers')


for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)

#dict that holds the entire order content 
order = {}

#represents if we're currently working on adding an item to order 
currentlyBuilding = False 
#the current item we're adding to order 
currentItem = None
#The number of the current items to add to the order (i.e: how many of those cheeseburgers to add)
	# This will change with each item we add to the order
numOfItemsToAdd = 1

def beginOrder(isRepeatRequest):
	currentlyBuilding = True
	#initiate automated greeting
	if (isRepeatRequest):
		engine.say("I'm sorry, please repeat that.")
	else:
		engine.say("Welcome to grill casa, what can I get for you?")
	engine.runAndWait()

	#begin listening for customer response
	with sr.Microphone() as source:
		print("Say something!")
		audio = recognizer.listen(source)
		
		#send to parser 
		response = parseResponse(audio)

		#if response is not an empty string, we should send it off to the nlp land

		#then pass it off to actually find the item of interest
		menuItem = menu.findProperBaseItem(response)

		if (menuItem != None):
			#determine if we need customizations or not 
			hasCustomizations = menu.itemHasCustomizations(menuItem)	
			if (hasCustomizations):
				#Begin the appropriate customization flow
			else:
				#Simply add item to the order	



#Takes the customer response we've got from the 
#microphone and passes it to the nlp engine to pull whatever 
#helpful info we can get 
def parseResponse(customerResponse):
	response = ''
	# recognize speech using Sphinx
	try:
		response = recognizer.recognize_sphinx(customerResponse)
		print("Sphinx thinks you said " + response)
	except sr.UnknownValueError:
		print("Sphinx could not understand audio")
		#ask them to repeat
		beginOrder(True)
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))	

	return response	

def findImportantDetails(customerResponse):
	#check for things like, how many of the main item do they want
	pass

def findMainItem(customerResponse):
	words = customerResponse.split(" ")
	for word in words:
		print(word)


beginOrder(False)
