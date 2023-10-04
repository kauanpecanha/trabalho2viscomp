import numpy as np
import cv2

image = cv2.imread(r"./provaA/cartaov2.png")

def recognizeMarked(image):

  newImage = image.copy()
  gab = []
  
  # for i in range(1, 26, 1): # loop responsável por exibir cada uma das questões da coluna
  #   print(f"{200+int((i-1)*(570-200)/25)}:{200+int((i)*(570-200)/25)}")
  #   cv2.waitKey(1000)
  
  # for i in range(1, 6, 1):
  #   cv2.imshow("", image[200:222, 62+(int((i-1)*(122-62)/5)):62+(int((i)*(122-62)/5))])
  #   cv2.waitKey(5000)
  
  # cv2.imshow("", newImage[200:570, 62:488])
  # cv2.waitKey(10000)
  
  # primeira coluna:
  # cv2.imshow("", newImage[:, 62:122])
  # cv2.waitKey(10000)


  # segunda coluna:
  # cv2.imshow("", newImage[:, 148:248])
  # cv2.waitKey(10000)
  
  # terceira coluna
  # cv2.imshow("", newImage[:, 306:366])
  # cv2.waitKey(10000)

  # quarta coluna
  # cv2.imshow("", newImage[:, 428:488])
  # cv2.waitKey(10000)

  for i in [0, 1, 2, 3]:
    for j in range(1, 26, 1):
      for k in range(1, 6, 1):
        photoA = newImage[].copy()
        photoB = newImage[].copy()
        photoC = newImage[].copy()
        photoD = newImage[].copy()
        photoE = newImage[].copy()

#   black = []

#   grayA = cv2.cvtColor(photoA, cv2.COLOR_BGR2GRAY)
#   grayB = cv2.cvtColor(photoB, cv2.COLOR_BGR2GRAY)
#   grayC = cv2.cvtColor(photoC, cv2.COLOR_BGR2GRAY)
#   grayD = cv2.cvtColor(photoD, cv2.COLOR_BGR2GRAY)
#   grayE = cv2.cvtColor(photoE, cv2.COLOR_BGR2GRAY)

#   _, limA = cv2.threshold(grayA, 230, 255, cv2.THRESH_BINARY)
#   _, limB = cv2.threshold(grayB, 230, 255, cv2.THRESH_BINARY)
#   _, limC = cv2.threshold(grayC, 230, 255, cv2.THRESH_BINARY)
#   _, limD = cv2.threshold(grayD, 230, 255, cv2.THRESH_BINARY)
#   _, limE = cv2.threshold(grayE, 230, 255, cv2.THRESH_BINARY)

#   black.append(np.sum(limA == 0))
#   black.append(np.sum(limB == 0))
#   black.append(np.sum(limC == 0))
#   black.append(np.sum(limD == 0))
#   black.append(np.sum(limE == 0))

#   indice = np.where(max(black))[0][0]
#   gab.append(indice)
#   return gab

recognizeMarked(image)