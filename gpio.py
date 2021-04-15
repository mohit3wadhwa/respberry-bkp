import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(40,GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(40,GPIO.HIGH)
    print("LED on")
    time.sleep(1)
    GPIO.output(40,GPIO.LOW)
    time.sleep(1)
    print("LED off")
    