import cv2
import numpy as np
import time

# Boş beyaz tuval
canvas = np.ones((512, 512, 3), dtype="uint8") * 255

print("Tuslar: L=Çizgi, C=Daire, R=Dikdörtgen, T=Yazi, E=Temizle, S=Kaydet, Q=Cikis")

while True:
    cv2.imshow("Keyboard Draw", canvas)
    key = cv2.waitKey(0) & 0xFF

    if key == ord("l"):
        cv2.line(canvas, (50, 50), (450, 50), (255, 0, 0), 3)
    elif key == ord("c"):
        cv2.circle(canvas, (256, 256), 100, (0, 255, 0), 3)
    elif key == ord("r"):
        cv2.rectangle(canvas, (100, 350), (400, 450), (0, 0, 255), 3)
    elif key == ord("t"):
        cv2.putText(canvas, "OpenCV", (180, 300),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif key == ord("e"):
        canvas = np.ones((512, 512, 3), dtype="uint8") * 255
    elif key == ord("s"):
        filename = f"outputs/draw_{time.strftime('%H%M%S')}.png"
        cv2.imwrite(filename, canvas)
        print("Kaydedildi:", filename)
    elif key == ord("q"):
        break

cv2.destroyAllWindows()
