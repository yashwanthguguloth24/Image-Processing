import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def linearoperation(img,P,L):
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

def color2gray(img):
    I=[]
    for i in range(0,len(img)):
        temp=[]
        for j in range(0,len(img[i])):
            t=img[i][j][0]+img[i][j][1]+img[i][j][2]
            temp.append(int(t/3))
        I.append(temp)
    return I

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

def log_compression(img):
    J=[]
    for i in range(0,len(img)):
        temp=[]
        for j in range(0,len(img[i])):
            temp.append(np.log2(int( 1+img[i][j] )) )
        J.append(temp)
    return J

def cdf(img):
    m=len(img)
    n=len(img[0])
    arr=[0]*256
    for i in range(0,len(img)):
        for j in range(0,len(img[i])):
            arr[img[i][j]]=arr[img[i][j]]+1
    pdf=[0]*256
    for i in range(0,len(arr)):
        pdf[i]=arr[i]/(m*n)
    cdf=[0]*256
    temp=0
    for i in range(0,len(cdf)):
        temp=temp+pdf[i]
        cdf[i]=temp
    return cdf

def fscs(img):
    A=min2d(img)
    B=max2d(img)
    res = linearoperation(img, 255/(B-A), (-255/(B-A))*A )
    return res

def histflat(img):
    img_cdf=cdf(img)
    J=[]
    for i in range(0,len(img)):
        temp=[]
        for j in range(0,len(img[i])):
            temp.append(img_cdf[img[i][j]])
        J.append(temp)
    res = fscs(J)
    histogram(res)

    

img = mpimg.imread('image.jpeg')
I=color2gray(img)

histflat(I)
plt.show()