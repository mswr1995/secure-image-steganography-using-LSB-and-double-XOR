import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.png',0)
stego_img = cv2.imread('lena2.png',0)

histr = cv2.calcHist([img],[0],None,[256],[0,256])
stego_histr = cv2.calcHist([stego_img],[0],None,[256],[0,256])

plt.plot(histr)
plt.show()
plt.plot(stego_histr)
plt.show()
