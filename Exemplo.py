import cv2
import matplotlib.pyplot as plt 
img = cv2.imread("carro.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img.shape

plt.imshow(img)
plt.show()