import cv2
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(BASE_DIR, '..', 'assets')
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'outputs')

img1 = cv2.imread(os.path.join(ASSET_DIR, 'doga.jpg'))
img2 = cv2.imread(os.path.join(ASSET_DIR, 'manzara.jpg'))
img3 = cv2.imread(os.path.join(ASSET_DIR, 'portre.jpg'))
img4 = cv2.imread(os.path.join(ASSET_DIR, 'sekil.png'))

img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2_hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
img3_gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

img1_rgb = cv2.convertScaleAbs(img1_rgb, alpha=1.2, beta=40)
img2_hsv[..., 2] = cv2.add(img2_hsv[..., 2], 50)
img3_gray = cv2.add(img3_gray, 30)

img1_resized = cv2.resize(img1_rgb, (300, 200))
img2_resized = cv2.resize(img2_hsv, (300, 200))
img3_resized = cv2.resize(img3_gray, (300, 200))
img4_resized = cv2.resize(img4, (300, 200))

rows, cols = img2_resized.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
img2_rotated = cv2.warpAffine(img2_resized, M, (cols, rows))

crop = img3_resized[50:150, 50:250]
crop = cv2.resize(crop, (300, 200))

img2_bgr = cv2.cvtColor(img2_rotated, cv2.COLOR_HSV2BGR)
crop_bgr = cv2.cvtColor(crop, cv2.COLOR_GRAY2BGR)
img1_bgr = cv2.cvtColor(img1_resized, cv2.COLOR_RGB2BGR)

top_row = np.hstack((img1_bgr, img2_bgr))
bottom_row = np.hstack((crop_bgr, img4_resized))
collage = np.vstack((top_row, bottom_row))

os.makedirs(OUTPUT_DIR, exist_ok=True)
cv2.imwrite(os.path.join(OUTPUT_DIR, 'collage_out.jpg'), collage)

cv2.imshow('Kolaj', collage)
cv2.waitKey(0)
cv2.destroyAllWindows()


