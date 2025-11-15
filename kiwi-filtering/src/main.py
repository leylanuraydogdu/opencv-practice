import cv2
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_PATH = os.path.join(BASE_DIR, "assets", "kiwi.jpg")
OUTPUT_PATH = os.path.join(BASE_DIR, "outputs", "kiwi_result.png")

def setup_dirs():
    os.makedirs(os.path.join(BASE_DIR, "assets"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "outputs"), exist_ok=True)


def load_image(path=ASSETS_PATH):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"❌ Dosya bulunamadı: {path}")
    return img

def create_kiwi_mask(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([30, 40, 40])
    upper_green = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    return mask

def create_binary_kiwi(img, mask):
    result = np.zeros_like(img)
    result[mask > 0] = [255, 255, 255]
    return result

def main():
    print(" İşleniyor...")

    setup_dirs()
    img = load_image()
    mask = create_kiwi_mask(img)
    final = create_binary_kiwi(img, mask)

    cv2.imwrite(OUTPUT_PATH, final)

    print(f"Tamamlandı! Çıktı oluşturuldu:\n   {OUTPUT_PATH}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("❌ HATA:", e)
