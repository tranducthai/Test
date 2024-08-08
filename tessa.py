import cv2
import numpy as np
from skimage.filters import threshold_local
import imutils
from skimage import measure
from skimage.measure import regionprops
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import tensorflow as tf
from tf_keras import Sequential
from tf_keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Flatten
import os
import easyocr

# Đọc và xử lý hình ảnh biển số
img_path = "C:/Users/thispc/Downloads/plate_1.jpg"
image = cv2.imread(img_path)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
V = hsv[:, :, 2]
reader = easyocr.Reader(['en'])
result = reader.readtext(V)

# In kết quả
for detection in result:
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    print("Detected text:", text)

    # Vẽ hình chữ nhật quanh chữ nhận diện được
    image = cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    image = cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Hiển thị ảnh với các chữ nhận diện được
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()