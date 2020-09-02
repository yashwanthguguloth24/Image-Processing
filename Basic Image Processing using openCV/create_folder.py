# create a folder of resized images 

import os
import sys
import fnmatch

listOfFiles = os.listdir('.')

if not os.path.exists('new_folder'):
    os.makedirs('new_folder')
    
for filename in listOfFiles:
    if fnmatch.fnmatch(filename,pattern):
        filename,new_img = resize(filename,400,600)
        cv2.imwrite("new_folder\\"+filename,new_img)
