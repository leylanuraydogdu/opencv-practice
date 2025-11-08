import numpy as np
import cv2
import os


def create_low_contrast_image(output_dir="../assets", filename="low_contrast_input.png"):
    """Düşük kontrastlı test görüntüsü oluşturur ve kaydeder."""
    os.makedirs(output_dir, exist_ok=True)

    size = 256         # Görsel boyutu
    mean = 125         # Ortalama parlaklık
    std_dev = 10       # Parlaklık değişimi (kontrast seviyesi)

    # Normal dağılımlı düşük kontrastlı görsel oluştur
    img_float = np.random.normal(mean, std_dev, (size, size))
    img = np.clip(img_float, 0, 255).astype(np.uint8)

    # Kaydet
    save_path = os.path.join(output_dir, filename)
    cv2.imwrite(save_path, img)

    print(f"✅ Düşük kontrastlı test görüntüsü oluşturuldu: {save_path}")
    return save_path


if __name__ == "__main__":
    create_low_contrast_image()