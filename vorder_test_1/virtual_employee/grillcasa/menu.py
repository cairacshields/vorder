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
	
	foundItem = False
	wantedItem = False


	
	for menuItem in getAllMenuItems():
		matches = 0
		print(menuItem.split(" "))
		for menuItemWord in menuItem.split(" "):
			for word in response:
				print(word)
				sq = SequenceMatcher(None, word, menuItemWord)
				print(sq.ratio())
				
				if(word == menuItemWord or sq.ratio() > .8):
					print("same word or match")
				else:
					print("not same")

         		# print '%-7s %-10s %f' % (word,menuItemWord,sq.ratio())

	# for wordInCustomerResponse in splitSentence:
	# 	#print(menuItem)
	# 	#search the user sentence for the current menuItem (must contain all menu item text)
	
	# 	for menuItem in getAllMenuItems():
	# 		splitMenuItem = menuItem.split(" ")
	# 		if (foundItem == False):
	# 			for splitItem in splitMenuItem:
	# 				print(splitItem)
	# 				print(wordInCustomerResponse)
	# 				sq.set_seqs(splitItem,wordInCustomerResponse)
 #        			print '%-7s %-10s %f' % (splitItem,wordInCustomerResponse,sq.ratio())

 #        			if (splitItem is wordInCustomerResponse or sq.ratio() > .8):
 #        				#accurate match
 #        				print("match")
 #        				foundItem = True
 #        				wantedItem = menuItem
 #        			else:
 #        				foundItem = False	
 #        				wantedItem = False
 #        	else:
 #        		print(foundItem)
 #        		return wantedItem			

		#print(foundItem)		



def getAllMenuItems():
	return {
		# itemName           hasCustomizations        basePrice        parentFoodChain
		"cheeseburger": {"hasCustomizations": True, "price": 3.99, "foodChain": "grillcasa"},
		"fries": {"hasCustomizations": True, "price": 1.99, "foodChain": "grillcasa"},
		"apple pie": {"hasCustomizations": False, "price": 0.99, "foodChain": "grillcasa"},
		"chicken nuggets": {"hasCustomizations": True, "price": 0.0, "foodChain": "grillcasa"},
	}


findProperBaseItem("hey can i have a ten piece chicken nugget?")