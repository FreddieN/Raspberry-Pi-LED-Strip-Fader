#this file has all pi specific functions removed so can be used on a normal pc
from __future__ import division #Pi runs Python 2.7

#Defining pins for easier readability
RED_PIN   = 23
GREEN_PIN = 18
BLUE_PIN  = 24

RGB = [0,0,0] #Setting the RGB variable any changes to this variable reflects to the live strip

#standard imports
import time

#defining the function that fades the colours
def fadeTo(target, time1):
    difference = [0,0,0] #I used the distance, speed and time equation to calculate how fast the strip needs to change. The "difference" is the distance.
    speed = [0, 0, 0]
    direction = [0,0,0] # this defines whether the RGB colours are going up or down.
	#putting the difference values into the arrays
    difference[0] = abs(RGB[0]-target[0])
    difference[1] = abs(RGB[1]-target[1])
    difference[2] = abs(RGB[2]-target[2])
	#putting the speed values into the arrays
    speed[0] = difference[0] / time1
    speed[1] = difference[1] / time1
    speed[2] = difference[2] / time1
	#this calculates the direction the colours need to go
    if(target[0] < RGB[0]):
        direction[0] = -1
    else:
        direction[0] = 1
    if(target[1] < RGB[1]):
        direction[1] = -1
    else:
        direction[1] = 1
    if(target[2] < RGB[2]):
        direction[2] = -1
    else:
        direction[2] = 1
		#debug prints
    print(direction)
    print(difference)
    print(speed)
	#this is the final stage, while the live strip (RGB) is not equal to the target colour we will continue running this loop.
    while int(round(RGB[0])) != target[0] or int(round(RGB[1])) != target[1] or int(round(RGB[2])) != target[2]:
        #Increasing the colours by how much they need to be changed per millisecond.
	RGB[0] += (direction[0] * speed[0]) / time1
        RGB[1] += (direction[1] * speed[1]) / time1
        RGB[2] += (direction[2] * speed[2]) / time1
        print(RGB)
        print(int(RGB[0]), int(RGB[1]), int(RGB[2]))
        time.sleep(0.001)
    return
	
#this is all I need for the actual colour changing, I can change the duration of the fade and how many colours the strip fades to. The colours are in RGB format.
while True:
	fadeTo([0, 60, 255], 50)
	time.sleep(5)
	fadeTo([20, 60, 255], 50)
	time.sleep(5)
	fadeTo([255, 161, 0], 50)
	time.sleep(5)
	fadeTo([255, 30, 0], 50)
	#debug
	#inputrgb = input("rgb")
	#inputtime = input("time")
	#fadeTo(inputrgb, inputtime)
