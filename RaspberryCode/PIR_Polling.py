#!/usr/bin/env python2.7
#########################################################
## PIR_Polling.py
## Created by Kenny from www.iotbreaks.vn, April 14, 2016.
## Released into the public domain.
## Tutorial: 
#########################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledOutPin=17
pirInPin=18

GPIO.setup(ledOutPin, GPIO.OUT)
GPIO.setup(pirInPin, GPIO.IN)

num=0
while 1 : 
	readValue = GPIO.input(pirInPin)
	print(str(num) + "readValue = " + str(readValue))
	num+=1
	GPIO.output(ledOutPin, readValue) 
	time.sleep(0.2)

GPIO.cleanup()