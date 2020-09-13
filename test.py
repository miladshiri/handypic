import cv2
import carve, basic, merg


if __name__ == '__main__':
    img = cv2.imread('testdata/p1.jpg')
    overlay = carve.circular(img)
    overlay = basic.rescale(overlay, 0.1)
    
    frame = basic.rescale(cv2.imread('testdata/p1.jpg'), .3)
    output = merg.place(overlay, frame, 570, 100)
    basic.imshow(output)
    