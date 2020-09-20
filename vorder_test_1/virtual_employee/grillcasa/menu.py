##
#
#
# Example of how to structure a foodchains menu so that it can work with our order_flow
#
#
#
##
from difflib import SequenceMatcher
from difflib import get_close_matches
import pyttsx
import speech_recognition as sr
import spacy
import customizations

#initialize the virtual ordering employee :)
engine = pyttsx.init()
voices = engine.getProperty('voices')    
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

#initialze the speech recognizer
recognizer = sr.Recognizer()

test_response = 'hi can i get two cheeseburgers' 

# nlp = spacy.load("en_core_web_sm")
# doc = nlp(u'hi can i get two cheeseburgers')


#Item we're currently working on 
selectedItem = {}


#Returns a finalized order item
def determineAndFinalizeItem(customerResponse):
	selectedItem = findProperBaseItem(customerResponse)
	
	quantity = getQuantity(customerResponse)

	findNegatives(customerResponse)

	#loop through the selectedItems customizations to ask the appropriate questions:
	for customization in getAllMenuItems().get(selectedItem):
		response = handleCustomization(customization)
		print(response)


	#return completed item
	return selectedItem	


#Returns a main (root level) menu item 
#This item is usually the parent of a meal that will require further configurations,
#or it is a single item that has no other configurations and stands on its own.
#Each level one menu item will return with it:
# 1. A boolean that tells us if we need to reach out and begin a customization flow 
# 2. The base price of the menu item (without any customization charges)
# 3. The associated foodChain (some items will have the same title, but belong to a different chain, this is important to distinguish for customization purposes)
def findProperBaseItem(customerResponse):
	#split the response in order to begin searching for the possible main item
	sq = SequenceMatcher(None)
	response = customerResponse.split(" ")
	
	wantedItem = False
	matches = 0
	
	for menuItem in getAllMenuItems():
		for menuItemWord in menuItem.split(" "):
			for word in response:
				print(word)
				sq = SequenceMatcher(None, word, menuItemWord)
				#print '%-7s %-10s %f' % (word,menuItemWord,sq.ratio())	
				
				if(word is menuItemWord or sq.ratio() > .8):
					print("same word or good enough match")
					matches += 1
					wantedItem = menuItem
					if (matches == len(menuItem.split(" "))):
						print("FOUND SOMETHING")
						print(wantedItem)
						return wantedItem		
				else:
					print("not same as menuItem")
					wantedItem = False		

def getQuantity(customerResponse):
	#searches the customer response to see if they've told us how many of the current items they want
	return 1 


def findNegatives(customerResponse):
	#Finds any elements that customers don't want on their item (i.e: no pickles)
	pass


def handleCustomization(customization):
	switcher = {
		"gender": customizations.getGender,
		"price": pricePlaceholder,
		"drink": customizations.configureDrink,
		"size": customizations.setSize,
		"sauce": customizations.addSauce,
		"side": customizations.setSide,
		"foodChain": foodChainPlaceholder
	}

	return switcher[customization]()




#region helper functions 	

def pricePlaceholder():
	pass

def foodChainPlaceholder():
	pass	

def itemHasCustomizations(item):
	return getAllMenuItems().get(item).get("hasCustomizations")


def getAllMenuItems():
	return {
		# itemName     hasCustomizations: (used for meals)    basePrice        parentFoodChain
		"cheeseburger": {"price": 3.99, "foodChain": "grillcasa"},
		"fries": {"size": "small", "price": 1.99, "foodChain": "grillcasa"},
		"apple pie": {"price": 0.99, "foodChain": "grillcasa"},
		"Quarter Pounder with Cheese": {"price": 0.0, "foodChain": "grillcasa"},
		"Sausage Burrito": {"price": 0.0, "foodChain": "grillcasa"},
		"Mocha Frappe": {"size": "small", "price": 0.0, "foodChain": "grillcasa"},
		"Double Quarter Pounder with Cheese": {"price": 0.0, "foodChain": "grillcasa"},
		"Big Mac": {"price": 0.0, "foodChain": "grillcasa"},
		"Quarter Pounder with Cheese Bacon": {"price": 0.0, "foodChain": "grillcasa"},
		"The Travis Scott": {"drink": None, "price": 0.0, "foodChain": "grillcasa"},
		"McDouble": {"price": 0.0, "foodChain": "grillcasa"},
		"Hamburger": {"price": 0.0, "foodChain": "grillcasa"},
		"Buttermilk Crispy Chicken Sandwich Meal": {"drink": None, "price": 0.0, "foodChain": "grillcasa"},
		"10 piece Chicken McNuggets Meal": {"drink": None, "sauce": None, "price": 0.0, "foodChain": "grillcasa"},
		"Double Quarter Pounder with Cheese Meal": {"drink": None, "price": 0.0, "foodChain": "grillcasa"},
		"Filet Fish Meal": {"drink": None, "price": 0.0, "foodChain": "grillcasa"},
		"Bacon Egg and Cheese McGriddles Meal": {"drink": None, "price": 0.0, "foodChain": "grillcasa"},
		"Sausage Burrito Meal": {"drink": None, "price": 0.0, "foodChain": "grillcasa"},
		"Hot Caramel Sundae": {"size": "small", "price": 0.0, "foodChain": "grillcasa"},
		"Hot Fudge Sundae": {"size": "small", "price": 0.0, "foodChain": "grillcasa"},
		"Chocolate Chip Cookie": {"price": 0.0, "foodChain": "grillcasa"},
		"Apple Slices": {"price": 0.0, "foodChain": "grillcasa"},
		"Hamburger Happy Meal": {"drink": None, "gender": None, "side": None, "price": 0.0, "foodChain": "grillcasa"},
		"Fanta Orange": { "price": 0.0, "foodChain": "grillcasa"},
		"Vanilla Shake": {"size": None, "price": 0.0, "foodChain": "grillcasa"},
	}


# endregion

determineAndFinalizeItem("hey can i have an Hamburger Happy Meal with no pickles and an apple pie")