import numpy as np
import cv2

img1 = cv2.imread( "../dataset/lena.pgm", 0)
img2 = cv2.medianBlur( img1, 3 )

cv2.imshow( "Original Image", img1 )	
cv2.imshow( "Median Filtering", img2 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()

cv2.imwrite( "output.bmp", img2 )