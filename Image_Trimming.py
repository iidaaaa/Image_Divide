import numpy as np
from PIL import Image
import cv2
import glob


input_path = r"\*.jpg"
out_path = r""

def first(im,h,w,i):
    i1 = "{0:04d}".format(i)
    name = out_path + "\\" + str(i1) + ".jpg"
    x = 0
    y = int(h/2)
    left = 0
    right = int(w/2)
    
    # img[top : bottom, left : right]
    dest = im[x:y,left:right]
    cv2.imwrite(name , dest)

def secound(im,h,w,i):
    i1 = "{0:04d}".format(i)
    name = out_path + "\\" + str(i1) + ".jpg"
    x = 0
    y = int(h/2)
    left = int(w/2)
    right = int(w)
    
    # img[top : bottom, left : right]
    dest = im[x:y,left:right]
    cv2.imwrite(name , dest)

def third(im,h,w,i):
    i1 = "{0:04d}".format(i)
    name = out_path + "\\" + str(i1) + ".jpg"
    x = int(h/2)
    y = h
    left = 0
    right = int(w/2)
    
    # img[top : bottom, left : right]
    dest = im[x:y,left:right]
    cv2.imwrite(name , dest)

def forth(im,h,w,i):
    i1 = "{0:04d}".format(i)
    name = out_path + "\\" + str(i1) + ".jpg"
    x = int(h/2)
    y = h
    left = int(w/2)
    right = int(w)
    
    # img[top : bottom, left : right]
    dest = im[x:y,left:right]
    cv2.imwrite(name , dest)


def main():
    i=0
    files = glob.glob(input_path)
    for f in files:
        i+=1
        print(f)
        im = cv2.imread(f)
        print(type(im))
        h,w,c=im.shape
        
        first(im,h,w,i)
        i+=1
        secound(im,h,w,i)
        i+=1
        third(im,h,w,i)
        i+=1
        forth(im,h,w,i)
        
if __name__ == "__main__":
    main()
