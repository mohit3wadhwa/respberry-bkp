import RPi.GPIO as GPIO
import tkinter
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT, initial=GPIO.LOW)


top = tkinter.Tk()



def turnOnLED():
    GPIO.output(40,GPIO.HIGH)
def turnOffLED():
    GPIO.output(40,GPIO.LOW)
    
B1 = tkinter.Button(top, text ="On", command = turnOnLED)
B2 = tkinter.Button(top, text ="Off", command = turnOffLED)

B1.pack()
B2.pack()
top.mainloop()
