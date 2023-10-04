import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

gab = []
# image = cv2.imread("/content/drive/MyDrive/Two/cartao.png")
image = []
def checkGabs(paths):
    checker = []
    for i in range(len(paths)):
        n = len(os.listdir(paths[i]))
        checker.append(n)
    
    if 0 in checker:
        print(f"Gabarito faltando em: {paths[checker.index(0)]}")
    else:
        print(f"Todos os gabaritos foram cadastrados corretamente.")


def recognizeMarked(image, lin0, lin1, col0, col1):

  newImage = image.copy()

  photoA = newImage[lin0:lin1,col0:col1].copy()
  photoB = newImage[lin0:lin1,col0:col1].copy()
  photoC = newImage[lin0:lin1,col0:col1].copy()
  photoD = newImage[lin0:lin1,col0:col1].copy()
  photoE = newImage[lin0:lin1,col0:col1].copy()

  black = []

  grayA = cv2.cvtColor(photoA, cv2.COLOR_BGR2GRAY)
  grayB = cv2.cvtColor(photoB, cv2.COLOR_BGR2GRAY)
  grayC = cv2.cvtColor(photoC, cv2.COLOR_BGR2GRAY)
  grayD = cv2.cvtColor(photoD, cv2.COLOR_BGR2GRAY)
  grayE = cv2.cvtColor(photoE, cv2.COLOR_BGR2GRAY)

  _, limA = cv2.threshold(grayA, 230, 255, cv2.THRESH_BINARY)
  _, limB = cv2.threshold(grayB, 230, 255, cv2.THRESH_BINARY)
  _, limC = cv2.threshold(grayC, 230, 255, cv2.THRESH_BINARY)
  _, limD = cv2.threshold(grayD, 230, 255, cv2.THRESH_BINARY)
  _, limE = cv2.threshold(grayE, 230, 255, cv2.THRESH_BINARY)

  black.append(np.sum(limA == 0))
  black.append(np.sum(limB == 0))
  black.append(np.sum(limC == 0))
  black.append(np.sum(limD == 0))
  black.append(np.sum(limE == 0))

  indice = np.where(max(black))[0][0]
  gab.append(indice)
  return gab

# recognizeMarked(image)

# identificar a versão da prova
def identifyTestVersion():
  # a = [11, 112, 211, 312, 414] old one
  a = [23, 124, 223, 324, 426] # new one
  # b = [19, 120, 219, 320, 422] old one
  b = [32, 133, 232, 333, 435] # new one

  black = []

  for i in ([0, 1, 2, 3, 4]):
    target = image[114:125, a[i]:b[i]]
    # cv2.imshow(target)
    gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    _, lim = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    black.append(np.sum(lim == 0))

  version = np.where(max(black))[0][0]
  return version

testVersion = identifyTestVersion()