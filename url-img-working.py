import cv2 
from PIL import Image
import requests
from io import BytesIO
import numpy as np

# Read image from url 
url = 'https://learnopencv.com/wp-content/uploads/2021/06/input_image-1.jpg'
response = requests.get(url)
img = np.array(Image.open(BytesIO(response.content)))

# Read static images
# img = cv2.imread('test-tiger.jpg')
# img = cv2.imread('test-bw.jpg')

# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0) 

# Convert to graycsale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

# Display Canny Edge Detection Image
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
