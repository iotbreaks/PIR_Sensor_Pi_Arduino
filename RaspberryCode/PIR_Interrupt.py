#!/usr/bin/env python2.7
#########################################################
## PIR_Interrupt.py
## Created by Kenny from www.iotbreaks.vn, April 14, 2016.
## Released into the public domain.
## Tutorial: 
#########################################################

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledOutPin=17
pirInPin=18
readValue=0 # default is 0 as PIR sensor deactivated

GPIO.setup(ledOutPin, GPIO.OUT)
GPIO.setup(pirInPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  

def pirSensorDidChange(pin): 
	print("Detect changed of PIR sensor to " + str(GPIO.input(pirInPin)))
	readValue = GPIO.input(pirInPin)
	GPIO.output(ledOutPin, readValue)

GPIO.add_event_detect(pirInPin, GPIO.BOTH, callback=pirSensorDidChange)
	
try:
	GPIO.output(ledOutPin, readValue)
	print("Detecting....")
	raw_input("Press anykey to finish>")  

except KeyboardInterrupt:  
    GPIO.cleanup() # clean up GPIO on CTRL+C exit 

GPIO.cleanup()
