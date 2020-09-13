##
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
#
#
##
import pyttsx

test_response = 'hi can i get two cheeseburgers' 

def beginOrder():
	#initiate automated greeting
