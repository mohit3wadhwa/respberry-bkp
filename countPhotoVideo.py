import shutil
import os

def get_count():
    source1 = os.listdir("/home/pi/Desktop/CCTV/photos")
    source2 = os.listdir("/home/pi/Desktop/CCTV/videos")
    
    list1 = []
    list2 = []
    var1 = ''
    var2 = ''
    
    for photofiles in source1:
        list1.append(photofiles)
    var1 = str(len(list1))
    
    for videofiles in source2:
        list2.append(videofiles)
    var2 = str(len(list2))
    
    return var1+','+var2
    
    