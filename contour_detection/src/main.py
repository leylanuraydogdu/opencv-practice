import cv2
import numpy as np
import os

input_path = "../assets/input.jpg"
output_path = "../outputs/result.jpg"

#  Görüntü yükleme 
img = cv2.imread(input_path)
if img is None:
    print("HATA: Görüntü bulunamadı.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

#  TrackBar fonksiyonu 
def nothing(x):
    pass

#  Pencere ve TrackBar oluştur
cv2.namedWindow("Kontur Analizi")
cv2.createTrackbar("Alt Eşik", "Kontur Analizi", 50, 255, nothing)
cv2.createTrackbar("Üst Eşik", "Kontur Analizi", 150, 255, nothing)

while True:
    low = cv2.getTrackbarPos("Alt Eşik", "Kontur Analizi")
    high = cv2.getTrackbarPos("Üst Eşik", "Kontur Analizi")

    # Kenar tespiti
    edges = cv2.Canny(blur, low, high)

    # Boşlukları kapat 
    kernel = np.ones((3, 3), np.uint8)
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Konturları bul 
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_copy = img.copy()
    count = 0

    for c in contours:
        area = cv2.contourArea(c)
        if area < 400:  # çok küçük alanları atla
            continue

        count += 1
        cv2.drawContours(img_copy, [c], -1, (0, 255, 0), 2)

        # Merkez noktası
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(img_copy, (cx, cy), 4, (255, 0, 0), -1)
            cv2.putText(img_copy, str(count), (cx - 10, cy - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Nesne sayısını ekle 
    cv2.putText(img_copy, f"Nesne Sayisi: {count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Yan yana göster 
    combined = np.hstack((cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR), img_copy))
    cv2.imshow("Kontur Analizi", combined)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC çıkış
        break

cv2.destroyAllWindows()


os.makedirs("../outputs", exist_ok=True)
cv2.imwrite(output_path, img_copy)
print(f"Sonuç kaydedildi: {output_path}")

