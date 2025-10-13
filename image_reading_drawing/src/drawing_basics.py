import cv2
import numpy as np
import os

# Dizin ayarları
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, '..', 'outputs')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Beyaz tuval
canvas = np.ones((512, 512, 3), dtype="uint8") * 255

# Temel çizimler
cv2.line(canvas, (50, 50), (450, 50), (255, 0, 0), 3)          # Mavi çizgi
cv2.circle(canvas, (256, 256), 100, (0, 255, 0), 3)            # Yeşil daire
cv2.rectangle(canvas, (100, 350), (400, 450), (0, 0, 255), 3)  # Kırmızı dikdörtgen
cv2.putText(canvas, "OpenCV", (180, 300),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)         # Siyah yazı

# Göster
cv2.imshow("Cizimler", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kaydet 
output_path = os.path.join(OUTPUT_DIR, "drawing_basics.png")
cv2.imwrite(output_path, canvas)
print("Kaydedildi:", output_path)
