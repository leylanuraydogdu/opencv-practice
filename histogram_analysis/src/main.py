import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# --- 1. Görüntüyü yükle ---
def load_image(path):
    """Görüntüyü grayscale olarak yükler."""
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError(f"Görüntü bulunamadı: {path}")
    return image


# --- 2. Histogram hesaplama ---
def compute_histogram(image):
    """Histogram hesaplar ve döndürür."""
    return cv2.calcHist([image], [0], None, [256], [0, 256])


# --- 3. Histogram eşitleme (kontrast artırma) ---
def equalize_contrast(image):
    """Histogram eşitleme uygular (kontrast düzeltme)."""
    return cv2.equalizeHist(image)


# --- 4. Histogramları çiz ve kaydet ---
def plot_histograms(original_hist, equalized_hist, save_path):
    """Orijinal ve eşitlenmiş histogramları yan yana çizer."""
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.title("Original Histogram")
    plt.plot(original_hist, color='gray')
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    plt.subplot(1, 2, 2)
    plt.title("Equalized Histogram")
    plt.plot(equalized_hist, color='black')
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


# --- 5. Görselleri karşılaştır ve kaydet ---
def compare_and_save(original, equalized, save_path):
    """Orijinal ve eşitlenmiş görüntüleri yan yana kaydeder."""
    comparison = np.hstack((original, equalized))
    cv2.imwrite(save_path, comparison)


# --- 6. Ana akış ---
def main():
    ASSETS_DIR = "../assets"
    OUTPUTS_DIR = "../outputs"

    os.makedirs(OUTPUTS_DIR, exist_ok=True)

    image_path = os.path.join(ASSETS_DIR, "low_contrast_input.png")  # test görseli
    gray = load_image(image_path)

    # 1. Orijinal histogramı hesapla
    hist_original = compute_histogram(gray)

    # 2. Histogram eşitleme (otomatik kontrast düzeltme)
    equalized = equalize_contrast(gray)

    # 3. Yeni histogramı hesapla
    hist_equalized = compute_histogram(equalized)

    # 4. Histogramları çiz ve kaydet
    plot_histograms(hist_original, hist_equalized, os.path.join(OUTPUTS_DIR, "histograms.png"))

    # 5. Görselleri karşılaştır ve kaydet
    compare_and_save(gray, equalized, os.path.join(OUTPUTS_DIR, "comparison.png"))

    # 6. Sonucu göster
    cv2.imshow("Original vs Equalized", np.hstack((gray, equalized)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("✅ İşlem tamamlandı! Histogram ve karşılaştırma görselleri 'outputs' klasöründe kaydedildi.")


if __name__ == "__main__":
    main()