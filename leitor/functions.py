import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

gab = []
# image = cv2.imread("/content/drive/MyDrive/Two/cartao.png")
image = []

# função que verifica se todos os arquivos de gabarito foram cadastrados corretamente, devendo ele receber uma list
# função plenamente funcioanal, favor não mexer
def checkGabs(paths):
    checker = []
    for i in range(len(paths)):
        n = len(os.listdir(paths[i]))
        checker.append(n)
    
    if 0 in checker:
        print(f"Gabarito faltando em: {paths[checker.index(0)]}")
    else:
        print(f"Todos os gabaritos foram cadastrados corretamente.")


def defineGabarito(archieve):
  image = archieve.copy() # copia o arquivo ong recebido
  for f in ([0, 1, 2]): # para cada uma das colunas
    g = [188, 310, 432]
    h = [248, 370, 492]

    for i in range(190, 340, 15): # primeiras parte da coluna
      recognizeMarked(image[i:i+15, g[f]:h[f]], i, i+15, g[f], h[f])
    for i in range(340, 430, 14): # segunda parte da coluna
      recognizeMarked(image[i:i+15, g[f]:h[f]], i, i+15, g[f], h[f])
    for i in range(440, 550, 15): # terceira parte da coluna
      recognizeMarked(image[i:i+15, g[f]:h[f]], i, i+15, g[f], h[f])
    print("\n")


# identificar a versão da prova - função plenamente funcional favor não mexer
def identifyTestVersion(archieve_path):
  # generalGabarito = []
  # for archieve_path in archieve_path_list:
  image = cv2.imread(archieve_path)
  a = [23, 124, 223, 324, 426] # new one
  b = [32, 133, 232, 333, 435] # new one

  black = []

  for i in ([0, 1, 2, 3, 4]):
    target = image[114:125, a[i]:b[i]]
    # cv2.imshow(target)
    gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    _, lim = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    black.append(np.sum(lim == 0))

  version = np.where(max(black))[0][0]
    # generalGabarito.append(defineGabarito(archieve_path)) # armazena o gabairto daquela versão na lista de gabaritos gerais