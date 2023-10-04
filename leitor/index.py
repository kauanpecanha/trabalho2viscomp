import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from functions import identifyTestVersion, checkGabs
from paths import *

# primeira fase - checkagem de presença de gabaritos
checkGabs([provaA_path, provaB_path, provaC_path, provaD_path, provaD_path, provaE_path])

# segunda fase - identificação da prova, e seu gabarito, para cada uma das versões
versao = identifyTestVersion(r"./provaA/cartaov2.png")
print(versao)