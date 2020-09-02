import cv2

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

def blurr(image):
    kernals = [3,5,9,11] # kernels
    for idx,k in enumerate(kernals):
        new_img = cv2.blur(image,ksize = (k,k))
        cv2.imshow(str(k),new_img)
        cv2.waitKey(0)
        
blurr(new_image)
