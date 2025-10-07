import cv2

img = cv2.imread("assets/portre.jpg")


cv2.imshow("Gorsel", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("outputs/portre_out.jpg", img)
print("Kaydedildi: outputs/portre_out.jpg")
