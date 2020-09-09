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


menuMap = parseMenu()

# create display object
disp = libscreen.Display(disptype='psychopy', dispsize=(900,600)) 

# create eyetracker object
tracker = eyetracker.EyeTracker(disp)

# create logfile object
log = liblog.Logfile()

# create screens
mainScreen = libscreen.Screen(fgc=(0, 191, 255), dispsize=(900,600))
mainScreen.draw_rect(colour=(0, 191, 255))
#mainScreen.draw_text(text="When you see a cross, look at it and press space. Then make an eye movement to the black circle when it appears.\n\n(press space to start)", fontsize=24)
mainScreen.draw_image(image="/Users/cairashields/Downloads/PyGaze-master/examples/vorder_test_1/test_menu_images/menu_image.png")

#stores the amount of blinks that fall within a microsecond apart
blinkCount = 0

#Menu Coordinate values 
#findFood(45, 300)


# calibrate eye tracker
tracker.calibrate()
print(tracker.connected())

def on_click(x, y, button, pressed):
	print("Mouse clicked")
	print("Food item found: %s" %(x))
	print(tracker.sample())
	#print("gazePosition_X: %s and gazePosition_Y: %s" %(tracker.sample()[0], tracker.sample()[1]))
	#findFood(45, 300)


# Should return the closest item on the menu to where the customers current gave it
def findClosestItem(x, y):
	for key in menuMap:
		itemDict = menuMap[key]
		if ((itemDict[0][0] < x and itemDict[0][1] > x) and (itemDict[1][0] < y and itemDict[1][1] > y)):
			return key

print(findClosestItem(48, 73))



# show menu for infinate amount of time 
while True:
	disp.fill(mainScreen)
	disp.show()


	time, startpos = tracker.wait_for_fixation_end()
	print(startpos)
	findFood(startpos[0], startpos[1])

	with mouse.Listener(on_click=on_click) as listener:
    		listener.join()



# # region helper functions 
# def breakDownDisplay():
#   print("Closing everything down...")
#   # end the experiment
#   log.close()
# 	disp.fill(screen = mainScreen)
# 	disp.show()
# 	#print tracker.sample()
#   tracker.close()
#   disp.close()
#   libtime.expend()

# def prinPos():
#   threading.Timer(5.0, prinPos).start()
#   print "Hello"
#   print tracker.sample()


#Start Position printing
# prinPos()  


