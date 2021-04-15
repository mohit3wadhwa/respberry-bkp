import shutil
import os

def get_image_file():
    source = os.listdir("/home/pi/Desktop/CCTV/photos")
    list1 = []
    for files in source:
        list1.append(files)
    list1 = sorted(list1, reverse = True)
    
    return list1[0]