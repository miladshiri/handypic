import cv2
import numpy as np 
from basic import imshow, rescale 

def circular(img):
    if img.shape[2] < 4:
        img = np.concatenate(
                [
                    img,
                    np.ones((img.shape[0], img.shape[1], 1), dtype = img.dtype) * 255
                ],
                axis = 2,
            )
    mask = np.zeros_like(img[:, :, 3])
    cv2.circle(mask, (int(img.shape[1]/2), int(img.shape[0]/2)), min(int(img.shape[1]/2), int(img.shape[0]/2)), color=(1, 1, 1), thickness=-1)
    img[:, :, 3] = mask * img[:, :, 3]
    return img

 