# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X3bS6xLLxEdU7OVlNpyU96mpcM7HJLEm
"""

"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11I6AXXfcSLil0MhQvqvD41Iv0isP2hTc
"""



"""from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("photo_2023-11-06_20-19-53.jpg")
cv2_imshow(rasm)
"""

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("photo_5901337244717921920_y.jpg")
cv2_imshow(rasm)

"""oqqora=cv2.cvtcolor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
"""

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm1=cv2.imread("photo_5777492618652005113_y.jpg")
cv2_imshow(rasm1)

oqqora=cv2.cvtColor(rasm1,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm2=cv2.imread("photo_5840480543135870789_y.jpg")
cv2_imshow(rasm2)

oqqora=cv2.cvtColor(rasm2,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm3=cv2.imread("photo_5845104354602890830_w.jpg")
cv2_imshow(rasm3)

oqqora=cv2.cvtColor(rasm3,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm4=cv2.imread("photo_5772648909154399269_x.jpg")
cv2_imshow(rasm4)

oqqora=cv2.cvtColor(rasm4,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)