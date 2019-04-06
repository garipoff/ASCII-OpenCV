import cv2
import numpy as np
import matplotlib.pyplot as plt

# Прописываем путь до нашего изображения
img = cv2.imread('1.jpeg')

ft = cv2.freetype.createFreeType2()

# Прописываем путь до нашего шрифта
ft.loadFontData(fontFileName='times.ttf', id=0)

# Сам текст и параметры его написания
ft.putText(img=img,
           text='СЧАСТЬЕ (´• ω •)',
           org=(15, 70),
           fontHeight=34,
           color=(255, 255, 255),
           thickness=-1,
           line_type=cv2.LINE_AA,
           bottomLeftOrigin=True)

cv2.imwrite('freetype.png', img)
img = cv2.imread('freetype.png')
cv2.imshow('freetype', img)

# На Ubuntu OpenCV может может выдать ошибку (на Windows всё нормально). В этом случае воспользуйся plt
#plt.imshow(img, interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])
#plt.show()

cv2.waitKey(0)