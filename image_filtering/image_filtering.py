import cv2
import numpy as np
import os

# --- Klasör ayarları ---
input_folder = "../assets"     # fotoğraflar assets klasörüne kaydolucak
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

# --- Görüntü listesi ---
images = ["img1.jpg", "img2.jpg", "img3.jpg"]

# --- Yardımcı fonksiyonlar ---
def stack_images(img_list):
    """Yan yana birleştirme"""
    min_height = min(img.shape[0] for img in img_list)
    resized = [cv2.resize(img, (int(img.shape[1]*min_height/img.shape[0]), min_height)) for img in img_list]
    return cv2.hconcat(resized)

def put_label(img, text):
    """Üstte başlık yazar"""
    labeled = img.copy()
    cv2.rectangle(labeled, (0, 0), (labeled.shape[1], 30), (0, 0, 0), -1)
    cv2.putText(labeled, text, (10, 22), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return labeled

# --- Filtreleme işlemleri ---
for i, name in enumerate(images, start=1):
    path = os.path.join(input_folder, name)
    img = cv2.imread(path)
    if img is None:
        print(f"Görüntü okunamadı: {path}")
        continue

    # Bulanıklaştırma
    gaussian = cv2.GaussianBlur(img, (5, 5), 0)
    median = cv2.medianBlur(img, 5)
    bilateral = cv2.bilateralFilter(img, 9, 75, 75)
    denoised = cv2.fastNlMeansDenoisingColored(img, None, 7, 7, 7, 21)

    blur_stack = stack_images([
        put_label(img, "Original"),
        put_label(gaussian, "Gaussian"),
        put_label(median, "Median"),
        put_label(bilateral, "Bilateral"),
        put_label(denoised, "Denoised")
    ])
    cv2.imwrite(os.path.join(output_folder, f"image{i}_blurs.jpg"), blur_stack)

    # Kenar algılama
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.uint8(np.clip(cv2.magnitude(sobelx, sobely), 0, 255))
    canny = cv2.Canny(gray, 100, 200)

    edge_stack = stack_images([
        put_label(img, "Original"),
        put_label(cv2.cvtColor(sobel, cv2.COLOR_GRAY2BGR), "Sobel"),
        put_label(cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR), "Canny")
    ])
    cv2.imwrite(os.path.join(output_folder, f"image{i}_edges.jpg"), edge_stack)

    # Morfolojik işlemler
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    erode = cv2.erode(binary, kernel, iterations=1)
    dilate = cv2.dilate(binary, kernel, iterations=1)
    open_img = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
    close_img = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

    morph_stack = stack_images([
        put_label(cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR), "Binary"),
        put_label(cv2.cvtColor(erode, cv2.COLOR_GRAY2BGR), "Erode"),
        put_label(cv2.cvtColor(dilate, cv2.COLOR_GRAY2BGR), "Dilate"),
        put_label(cv2.cvtColor(open_img, cv2.COLOR_GRAY2BGR), "Open"),
        put_label(cv2.cvtColor(close_img, cv2.COLOR_GRAY2BGR), "Close")
    ])
    cv2.imwrite(os.path.join(output_folder, f"image{i}_morph.jpg"), morph_stack)

    print(f"{name} işlendi ✅") ,
    