import cv2
import numpy as np

# Beyaz tuval
canvas = np.ones((512, 512, 3), dtype="uint8") * 255

# Çizimler
cv2.line(canvas, (50, 50), (450, 50), (255, 0, 0), 3)
cv2.circle(canvas, (256, 256), 100, (0, 255, 0), 3)
cv2.rectangle(canvas, (100, 350), (400, 450), (0, 0, 255), 3)
cv2.putText(canvas, "OpenCV", (180, 300),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# Göster
cv2.imshow("Cizimler", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Kaydet
cv2.imwrite("outputs/drawing_basics.png", canvas)
print("Kaydedildi: outputs/drawing_basics.png")
