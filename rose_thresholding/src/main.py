import cv2
import numpy as np
import os

def setup_dirs():
    os.makedirs('assets', exist_ok=True)
    os.makedirs('outputs', exist_ok=True)

def load_image(path='assets/rose.jpg'):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"❌ '{path}' bulunamadı!")
    return img

def create_rose_mask(img):
    """Gül için maske oluştur"""
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Kırmızı renk aralıkları (daha geniş)
    mask1 = cv2.inRange(hsv, np.array([0, 30, 30]), np.array([15, 255, 255]))
    mask2 = cv2.inRange(hsv, np.array([165, 30, 30]), np.array([180, 255, 255]))
    mask = cv2.bitwise_or(mask1, mask2)
    
    # Maskeyi iyileştir
    kernel = np.ones((7, 7), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.GaussianBlur(mask, (7, 7), 0)
    
    return mask

def create_purple_rose(img, mask):
    """Siyah arka planda mor gül oluştur"""
    result = np.zeros_like(img)
    
    # Canlı mor renk (BGR formatında)
    purple = np.array([220, 20, 200])  # Daha canlı ve yoğun mor
    
    # Gülün her pikselini mor tona çevir
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if mask[y, x] > 0:
                # Orijinal pikselin parlaklığını al
                original_pixel = img[y, x]
                brightness = np.mean(original_pixel) / 255.0
                
                # Parlaklığı artır ve mor rengi uygula
                enhanced_brightness = min(brightness * 1.5, 1.0)  # %50 daha parlak
                
                # Mor rengi parlaklığa göre ayarla
                result[y, x] = (purple * enhanced_brightness * (mask[y, x] / 255.0)).astype(np.uint8)
    
    return result

def main():
    """Ana fonksiyon"""
    print("🔄 İşleniyor...")
    
    setup_dirs()
    img = load_image()
    
    mask = create_rose_mask(img)
    purple_rose = create_purple_rose(img, mask)
    
    cv2.imwrite('outputs/result.jpg', purple_rose)
    
    print("✅ Tamamlandı! Sonuç: outputs/result.jpg")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ HATA: {e}")