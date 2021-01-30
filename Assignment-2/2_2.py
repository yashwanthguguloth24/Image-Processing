import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def linearoperation(P,L):
    J=[]
    for i in range(0,len(img)):
        temp=[]
        for j in range(0,len(img[i])):
            a=int(P*img[i][j]+L)
            if (a>255):
                a=255
            if (a<0):
                a=0
            temp.append(a)
        J.append(temp)
    return J

def histogram(img):
    arr=[]
    for i in range(0,len(img)):
        for j in range(0,len(img[i])):
            arr.append(img[i][j])
    plt.hist(arr, color = 'blue', edgecolor = 'black',bins = int(1800))
    plt.title("Histogram")
    plt.xlim(0, 255)

def max2d(img):
    maxarr=[]
    for i in range(0,len(img)):
        maxarr.append(max(img[i]))
    
    return max(maxarr)

def min2d(img):
    minarr=[]
    for i in range(0,len(img)):
        minarr.append(min(img[i]))
    
    return min(minarr)

img = mpimg.imread('space.jpg')
img = img[:,:,0]

A=min2d(img)
B=max2d(img)

res = linearoperation( 255/(B-A), (-255/(B-A))*A ) 

print(min2d(res),max2d(res))

plt.figure(1)
histogram(img)

plt.figure(2)
histogram(res)

plt.show()