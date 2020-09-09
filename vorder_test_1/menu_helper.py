import pytesseract
import collections

from pytesseract import Output

from PIL import Image
import cv2


######
### TODO 
### 1. Convert images to grayscale for more accurate processing 
###
###
#####


#Returns a Tuple of ranges mapped to a String
def parseMenu():
	menuMap = {}
	img = cv2.imread("/Users/cairashields/Downloads/PyGaze-master/examples/vorder_test_1/test_menu_images/test_menu_2.jpeg")
	data = pytesseract.image_to_data(img, config='--psm 12', output_type=Output.DICT)
	
	n_boxes = len(data['level'])
	
	#Will be switched when the Y axis changes 
	firstRow = True

	#Current item values 
	# image_top_left =	(0,0)
 #    image_top_right =	(0,0)
 #    text_bottom_left =	(0,0)
 #    text_bottom_right =	(0,0)

	fullItemText = ''

	imageStartXPos = 0
	imageEndXPos = 0
	textStartXPos = 0
	textEndXPos = 0
	textYPos = 0

	imageYPos = 0

	for i in range(n_boxes):
			# Example: x = 33 y = 531 text = Subwhich
    		(x, y, w, h, text) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i], data['text'][i])
    		# print("%s %s %s" %(x,y,text))


    		if (len(text) > 2):
    			#consider it a possible menu item 
    			#Back-to-back text is treated as a single menu item
    			if (imageStartXPos == 0):
    				imageStartXPos = x

    			if (textStartXPos == 0):
    				textStartXPos = x	

    			#These values Must update with every iteration 	
    			imageEndXPos = x	
    			textEndXPos = x
    			
    			if (textYPos != y):
    				#new row 
    				imageYPos = y - textYPos	
    				if (imageYPos < 0):
    					imageYPos = 0
    				textYPos = y	

    			#Y axis should be 0 on images if we are on the first row
    			if ((image_top_left[1] != 0) and (image_top_right[1] != 0)):
    				#not on first row
    				firstRow = False

    			fullItemText += text

    		else:
    			#Save 

    			# if (firstRow):
    			# 	#no-op#
    			# else:
    			# 	#Y axis will not be 0	
    			
    			image_top_left = (imageStartXPos, imageYPos)
    			image_top_right = (imageEndXPos, imageYPos)

    			text_bottom_left = (textStartXPos, textYPos)
    			text_bottom_right = (textEndXPos, textYPos)

    			#Create the tuple and save item to map 
    			#A customers x gaze coordinate must fall within itemDict[0][0] and itemDict[0][1]
    			#Same for customers y gaze
    			itemDict = ((imageStartXPos, textEndXPos), (textYPos - 200, textYPos))

    			if (len(fullItemText) > 0):
    				menuMap[fullItemText] = itemDict

    			#then clear everything 	
    			imageStartXPos = 0
    			textStartXPos = 0
    			fullItemText = ''

    # A customers gaze coordinates, should hoepfully fall between 			
	print(menuMap)
	return menuMap


#Given Gaze Position is a Tuple (x,y)
def findFood():
	foodItem = 'not found'
	# gazePosition_X = gazePosition[0]
	# gazePosition_Y = gazePosition[1]

	img = cv2.imread("/Users/cairashields/Downloads/PyGaze-master/examples/vorder_test_1/test_menu_images/test_menu_2.jpeg")
	
	d = pytesseract.image_to_data(img, config='--psm 12', output_type=Output.DICT)
	# print(d)
	n_boxes = len(d['level'])
	
	for i in range(n_boxes):
			# Example: x = 33 y = 531 text = Subwhich
    		(x, y, w, h, text) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i], d['text'][i])
    		print("%s %s %s" %(x,y,text))

    		#Define appropriate ranges
    		x_range = range((x - 200), (x + 200))
    		y_range = range((y - 200), (y + 200))

			#Check if this is potentially the menu item customer is gazing at
    		# if ((gazePosition_X in x_range) and (gazePosition_Y in y_range)):
    		# 	foodItem = text
    		# 	print("Food item found: %s" %(foodItem))
    		# 	return foodItem

#findFood()
parseMenu()