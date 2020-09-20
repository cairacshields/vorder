##
#
# Once we have a base item, and we've determined that we 
# have further customizations (i.e: drink flavor, sauces, etc)
# we should get those set up and then send the item off to the main order.
#
#
#
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

# test_response = 'hi can i get two cheeseburgers' 

nlp = spacy.load("en_core_web_sm")
# doc = nlp(u'hi can i get two cheeseburgers')



# region prompt, parse, return 

def getGender():
  #ask for gender and return correct response 
  #print("Setting gender: girl")
  return "girl"


def configureDrink():
  #print("Configuring drink")
  return "drink"

def setSize():
  #print("Setting Size")
  return "small"  

def addSauce():
  #print("Adding Sauces")
  return "bbq"  

def setSide():
  #print("Setting side")
  return "apple slices"  






