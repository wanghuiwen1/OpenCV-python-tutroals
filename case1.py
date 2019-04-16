import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\Administrator\\Pictures\\20180522203809.jpg',0)

print(img)
# 读取图片
# cv2.imshow('微信图片_20180522203809.jpg',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#先创建窗口再加载图片
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 保存图片
# cv2.imwrite('messigray.png',img)


img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
