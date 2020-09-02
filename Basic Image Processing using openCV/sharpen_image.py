import cv2
import numpy as np

def resize(filename,width,height):
    image = cv2.imread(filename)
    cv2.imshow('Original image',image)
    cv2.waitKey(0)
    org_height , org_width = image.shape[0:2]
    print("width: ",org_width)
    print("height: ",org_height)

    if org_width >= org_height:
        new_image = cv2.resize(image,(width,height))
    else:
        new_image = cv2.resize(image,(height,width))

    return filename,new_image

filename,new_image = resize('bird.jpg',600,400)

def sharpen(image):
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    new_img = cv2.filter2D(image,-1,kernel)
    cv2.imshow('sharpened_img',new_img)
    cv2.waitKey()
    return new_img
  
final_img = sharpen(new_image)
