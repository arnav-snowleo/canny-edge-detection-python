# UNUSED CODE

import cv2 

# ----------------------------------------------------------------
# SCIKIT TRY - failed : urllib.error.HTTPError: HTTP Error 403: Forbidden
# from skimage import io

# url = 'http://answers.opencv.org/upfiles/logo_2.png'
# img = io.imread(url)

# -------------------------------------------------------------------------------

# ~~ sessionobj

# from random import seed
# import requests
 
# url = "https://www.gamefaqs.com"
# session_obj = requests.Session()
# response = session_obj.get(url, headers={"User-Agent": "Mozilla/5.0"})
 
# print(response.status_code)

# --------------------------------------------------------------------------------

# import urllib
# import numpy as np

# import urllib.request as url_req

# req = url_req.urlopen('http://answers.opencv.org/upfiles/logo_2.png')
# arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
# img = cv2.imdecode(arr, -1) # 'Load it as it is'

# --------------------------------------------------------------------------------

# import urllib
# import numpy as np

# import urllib.request as url_req

# from urllib.request import Request, urlopen

# req = Request('http://answers.opencv.org/upfiles/logo_2.png', headers={'User-Agent': 'Mozilla/5.0'})
# webpage = urlopen(req).read()

# print(webpage)

# req = url_req.urlopen('http://answers.opencv.org/upfiles/logo_2.png' , headers={'User-Agent': 'Mozilla/5.0'})
# arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
# img = cv2.imdecode(arr, -1) # 'Load it as it is'

# --------------------------------------------------------------------------------

# import cv2
# from urllib.request import urlopen
# import numpy as np

# req = urlopen('http://answers.opencv.org/upfiles/logo_2.png')
# arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
# img = cv2.imdecode(arr, -1) # 'Load it as it is'


# ----------------------------------------------

from PIL import Image
import requests
from io import BytesIO
import numpy as np

url = 'http://answers.opencv.org/upfiles/logo_2.png'
response = requests.get(url)
img = np.array(Image.open(BytesIO(response.content)))










































# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$----------------------------
# Read the original image

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
