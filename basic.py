import cv2
import numpy as np 

def imshow(image, title='figure'):
    img = image.copy()
    if img.shape[2] > 3:
        mask = img[:,:,3]/255.0
        img[:,:,0] = img[:,:,0] * mask
        img[:,:,1] = img[:,:,1] * mask
        img[:,:,2] = img[:,:,2] * mask
    cv2.imshow(title, img)

def rescale(image, scale):
    return cv2.resize(image, (int(image.shape[1]*scale), int(image.shape[0]*scale)))
   