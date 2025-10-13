import cv2
import os

# Dizin ayarları 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_PATH = os.path.join(BASE_DIR, '..', '..', 'assets', 'img1.jpg')
OUTPUT_PATH = os.path.join(BASE_DIR, '..', 'outputs', 'img1_out.jpg')

# Görseli oku
img = cv2.imread(ASSET_PATH)

if img is None:
    print("Görsel okunamadı! Dosya yolunu veya ismini kontrol et.")
else:
    # Görseli göster
    cv2.imshow("Görsel", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Görseli kaydet
    cv2.imwrite(OUTPUT_PATH, img)
    print(f"Kaydedildi: {OUTPUT_PATH}")