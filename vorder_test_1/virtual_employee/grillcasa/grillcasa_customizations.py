
##
# Example FoodChain specific customizations
# 
#
##


import pyttsx
import speech_recognition as sr
import spacy
from difflib import SequenceMatcher

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

def configureMeal(item):
  switcher = {
    "fries"
  }


def customizeFries(meal):
  #Determine the size fries and returns the meal with appropriate info
  pass  


def genericConfigurations(item):
  pass  