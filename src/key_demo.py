# -*- coding:utf-8 -*-
#import SH1106
import time
#import config
import traceback

import RPi.GPIO as GPIO

import time
import subprocess

#from PIL import Image
#from PIL import ImageDraw
#from PIL import ImageFont

#GPIO define
RST_PIN        = 25
CS_PIN         = 8
DC_PIN         = 24

KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13

KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16



#define KEY_UP_PIN      6
#define KEY_DOWN_PIN    19
#define KEY_LEFT_PIN    5
#define KEY_RIGHT_PIN   26
#define KEY_PRESS_PIN   13
#define KEY1_PIN        21
#define KEY2_PIN        20
#define KEY3_PIN        16


# 240x240 display with hardware SPI:
#disp = SH1106.SH1106()
#disp.Init()

# Clear display.
#disp.clear()

#init GPIO
# for P4:
# sudo vi /boot/config.txt
# gpio=6,19,5,26,13,21,20,16=pu
GPIO.setmode(GPIO.BCM) 
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Input with pull-up
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.

#image = Image.new('1', (disp.width, disp.height))

# Get drawing object to draw on image.
#draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
#draw.rectangle((0,0,disp.width,disp.height), outline=0, fill=0)
#disp.ShowImage(disp.getbuffer(image))

# try:
while 1:
    # with canvas(device) as draw:
    if not GPIO.input(KEY_UP_PIN): # button is released
        print "Up"
        
    if not GPIO.input(KEY_LEFT_PIN): # button is released
        print "left"
        
    if not GPIO.input(KEY_RIGHT_PIN): # button is released
        print "right"        
        
    if not GPIO.input(KEY_DOWN_PIN): # button is released
        print "down"
        
    if not GPIO.input(KEY_PRESS_PIN): # button is released
        print "center"
        
    if not GPIO.input(KEY1_PIN): # button is released
        print "KEY1"
        
    if not GPIO.input(KEY2_PIN): # button is released
        print "KEY2"
        
    if not GPIO.input(KEY3_PIN): # button is released
        print "KEY3"
        
    #disp.ShowImage(disp.getbuffer(image))
    
# except:
	# print("except")
# GPIO.cleanup()
