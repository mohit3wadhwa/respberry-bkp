from picamera import PiCamera
from sendEmail import send_email
from get_latest_photo import get_image_file
from countPhotoVideo import get_count
from time import sleep
import tkinter as tk
from tkinter import font
from tkinter import messagebox


top = tk.Tk()

#Variable Initialization 
i = 0
j = 0


def camPreviewPhoto():
    global i
    global j
    i =i+1
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/CCTV/photos/image%s.jpg' %i)
    camera.stop_preview()
    camera.close()
    send_email(get_image_file())

def camPreviewVideo():
    global i
    global j
    j =j+1
    i =i+1
    camera = PiCamera()
    camera.start_preview()
    camera.start_recording('/home/pi/Desktop/CCTV/videos/video%s.h264' %j)
    sleep(9)
    camera.stop_recording()
    sleep(3)
    camera.capture('/home/pi/Desktop/CCTV/photos/image%s.jpg' %i)
    camera.stop_preview()
    camera.close()
    send_email(get_image_file())


def raiseAlarm():
    messagebox.showinfo("Info", "Alarming is in progress...")


def countPhotoVideo():
    getcount =get_count()
    temp1, temp2 = getcount.split(",")
    messagebox.showerror("Count of Photos and Videos", "Photos: "+temp1+ "\n" "Videos: "+temp2)
    

def deletePhoto():
    messagebox.showinfo("Info", "Delete Photo feature is yet to come...")
def deleteVideo():
    messagebox.showinfo("Info", "Delete Video feature is yet to arrive...Stay tuned...")

helfont = font.Font(family ='Helvatica', size =9, weight ='bold')
#photo1 = tk.PhotoImage(file="camera3.png")
   
B1 = tk.Button(top, text ="PHOTO", font = helfont, width =27, height =15, command =camPreviewPhoto)
B2 = tk.Button(top, text ="VIDEO",font = helfont, width =27,height =15, command =camPreviewVideo)
B3 = tk.Button(top, text ="ALARM",font = helfont, width=27, height =15,command =raiseAlarm)
B4 = tk.Button(top, text ="COUNT PHOTO/VIDEO",font = helfont, width=27,height =15, command =countPhotoVideo)
B5 = tk.Button(top, text ="DELETE PHOTO",font = helfont, width=27,height =15, command =deletePhoto)
B6 = tk.Button(top, text ="DELETE VIDEO",font = helfont, width=27,height =15, command =deleteVideo)

B1.grid(row=0,column=0)
B2.grid(row=0,column=1)
B3.grid(row=0,column=2)
B4.grid(row=1,column=0)
B5.grid(row=1,column=1)
B6.grid(row=1,column=2)


top.mainloop()

