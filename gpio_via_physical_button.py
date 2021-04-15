import RPi.GPIO as GPIO
import tkinter
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        print(GPIO.input(11))
        GPIO.output(40,GPIO.input(11))
        
except KeyboardInterrupt:
    GPIO.cleanup()