# First trial of Vorder Menu EyeTracking 

# # # # #
# importing the relevant libraries
import random
import constants
import threading

from menu_helper import parseMenu
from pygaze import libscreen
from pygaze import libtime
from pygaze import liblog
from pygaze import libinput
from pygaze import eyetracker

from pynput import mouse

#pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tessdata'

menuMap = parseMenu()

# create display object
disp = libscreen.Display(disptype='psychopy', dispsize=(1200,800)) 

# create eyetracker object
tracker = eyetracker.EyeTracker(disp)

# create logfile object
log = liblog.Logfile()

# create screens
mainScreen = libscreen.Screen(dispsize=(1200,800))
#mainScreen.draw_text(text="When you see a cross, look at it and press space. Then make an eye movement to the black circle when it appears.\n\n(press space to start)", fontsize=24)
mainScreen.draw_image(image="./documents/vorder/vorder_test_1/test_menu_images/test_menu_2.jpeg")

#stores the amount of blinks that fall within a microsecond apart
blinkCount = 0


# calibrate eye tracker
tracker.calibrate()
print(tracker.connected())

#print("gazePosition_X: %s and gazePosition_Y: %s" %(tracker.sample()[0], tracker.sample()[1]))

# Should return the closest item on the menu to where the customers current gave it
def findClosestItem(x, y):
	print(tracker.sample())
	for key in menuMap:
		itemDict = menuMap[key]
		if ((itemDict[0][0] < x and itemDict[0][1] > x) and (itemDict[1][0] < y and itemDict[1][1] > y)):
			return key

#Some menu items come back incorrectly formatted 
def repairMenuItemString(item):
	print(item)
	slashPosition = item.find("\\")
	if (slashPosition != -1):
		#remove the backslash and return new repaired string
		return item[slashPosition:] 
	else:
		return item	

print(repairMenuItemString(findClosestItem(48, 73)))



# show menu for infinate amount of time 
while True:
	disp.fill(mainScreen)
	disp.show()

	#TODO - detect blinks 



# region helper functions 
def breakDownDisplay():
	print("Closing everything down...")
  	# end the experiment
  	log.close()
	disp.fill(screen = mainScreen)
	disp.show()
	#print tracker.sample()
  	tracker.close()
  	disp.close()
  	libtime.expend()

# def prinPos():
#   threading.Timer(5.0, prinPos).start()
#   print tracker.sample()


#Start Position printing
# prinPos()  


