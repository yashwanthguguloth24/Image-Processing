import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def color2gray(img):
    I=[]
    for i in range(0,len(img)):
        temp=[]
        for j in range(0,len(img[i])):
            t=img[i][j][0]+img[i][j][1]+img[i][j][2]
            temp.append(int(t/3))
        I.append(temp)
    return I

def Zoom(img):
    m=int(len(img)*1.5)
    n=int(len(img[0])*1.5)
    res=[]
    for i in range(0,m):
        temp=[]
        for j in range(0,n):
            temp.append(-1)
        res.append(temp)
    i_temp1=2
    j_temp1=2
    i_temp2=0
    j_temp2=0
    for i in range(0,len(res)):
        if(i==i_temp1):
            i_temp1=i_temp1+3
            continue
        else :
            for j in range(0,len(res[i])):
                if(j==j_temp1):
                    j_temp1=(j_temp1+3)%1536
                    continue
                else :
                    res[i][j]=img[i_temp2][j_temp2]
                    j_temp2=(j_temp2+1)%1024
            i_temp2=i_temp2+1

    for i in range(0,len(res)):
        for j in range(0,len(res[i])):
            if(res[i][j]==-1):
                if(i==0 and j!=len(res[i])-1):
                    res[i][j]=np.random.choice([res[i][j-1],res[i][j+1]])
                elif(i==0 and j==len(res[i])-1):
                    res[i][j]=res[i][j-1]
                elif(i!=0 and j==len(res[i])-1):
                    res[i][j]=np.random.choice([res[i-1][j],res[i][j-1]])
                else:
                    res[i][j]=np.random.choice([res[i-1][j],res[i][j-1],res[i][j+1]])

    return res
    

img = mpimg.imread('space.jpg')
I=color2gray(img)

res=Zoom(I)
imgplot=plt.imshow(res, cmap="gray")
plt.show()