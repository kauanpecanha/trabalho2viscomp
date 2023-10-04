import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
from functions import checkGabs, getGab
from paths import provaAgab_path, provaBgab_path, provaCgab_path, provaDgab_path, provaEgab_path

# gabA = cv2.imread(provaAgab_path)
# cv2.imshow("foto a", gabA)
# cv2.waitKey(1000)

# getGab(provaAgab_path)
getGab(r"./bubbleSheet.jpg")