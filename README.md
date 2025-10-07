OpenCV Görüntü İşleme Uygulamaları

Bu proje, OpenCV kütüphanesi kullanılarak temel görüntü işleme konularını uygulamalı olarak göstermektedir.
Amaç, görselleri okuyabilmek, gösterebilmek, üzerinde çizimler yapabilmek, klavye–fare etkileşimi kurabilmek ve temel görüntü işleme tekniklerini (renk uzayı, döndürme, kırpma, birleştirme vb.) kullanarak bir kolaj oluşturmaktır.

📂 Proje Yapısı
uygulama1/
│
├── assets/          → Örnek görseller (doga.jpg, manzara.jpg, portre.jpg, sekil.png)
├── outputs/         → İşlenmiş veya oluşturulmuş görsellerin kaydedildiği klasör
├── src/
│   ├── read_show_save.py     → Görsel okuma, gösterme ve kaydetme işlemleri
│   ├── drawing_basics.py     → Temel çizim fonksiyonları (çizgi, daire, dikdörtgen, metin)
│   ├── keyboard_draw.py      → Klavye ve fare etkileşimli çizim uygulaması
│   └── collage_maker.py      → Görüntü işleme temelleriyle kolaj oluşturma
├── requirements.txt  → Gerekli kütüphaneler
└── README.md

⚙️ Gereksinimler

Projeyi çalıştırmak için Python 3 ve aşağıdaki kütüphaneler gereklidir:

pip install opencv-python numpy


Eğer requirements.txt dosyan varsa:

pip install -r requirements.txt

🚀 Çalıştırma

Terminalde proje dizinine gir:

cd C:\opencv\uygulama1


(veya projenin bulunduğu klasör)

Varsa sanal ortamı etkinleştir:

.venv\Scripts\activate


Çalıştırmak istediğin dosyayı seç:

python src/read_show_save.py
python src/drawing_basics.py
python src/keyboard_draw.py
python src/collage_maker.py

🧩 Uygulama Açıklamaları
1️⃣ read_show_save.py

OpenCV’nin temel işlevlerini gösterir:

Görsel okuma: cv2.imread()

Görsel gösterme: cv2.imshow()

Görsel kaydetme: cv2.imwrite()

Görsellerin boyutu ve tipi ekrana yazdırılabilir.

OpenCV’de dosya girdi/çıktı işlemlerinin temellerini öğretir.

2️⃣ drawing_basics.py

OpenCV ile temel şekil çizimleri yapılır:

cv2.line() → çizgi çizme

cv2.rectangle() → dikdörtgen çizme

cv2.circle() → daire çizme

cv2.putText() → metin yazma

Renk, koordinat ve kalınlık gibi parametreler değiştirilerek denemeler yapılabilir.

Görüntü üzerine çizim yapmayı öğretir.

3️⃣ keyboard_draw.py

Klavye ve fare etkileşimiyle dinamik çizim yapılmasını sağlar.

Kullanıcı farklı tuşlara basarak farklı şekiller çizebilir (örneğin “r” tuşu → dikdörtgen, “c” tuşu → daire).

Fare tıklamaları algılanarak (cv2.EVENT_LBUTTONDOWN) çizim yapılır.

Gerçek zamanlı kullanıcı etkileşimini öğretir.

4️⃣ collage_maker.py

Görüntü işleme temellerinin tamamını içeren uygulamadır.

Yapılan işlemler:

Renk uzayları: RGB, HSV, Grayscale dönüşümleri

Piksel manipülasyonu: parlaklık ve kontrast ayarlama

Yeniden boyutlandırma (cv2.resize)

Döndürme (cv2.getRotationMatrix2D, cv2.warpAffine)

Kırpma (NumPy slicing)

Görselleri birleştirme (np.hstack, np.vstack)

Sonuç olarak 2x2 bir kolaj oluşturulur ve outputs/collage_out.jpg dosyasına kaydedilir.

Kolaj yapısı:

[ Doğa (RGB)           | Manzara (HSV + Döndürülmüş) ]
[ Portre (Kırpılmış)   | Şekil (Orijinal)           ]

🧠 Öğrenilen Konular

OpenCV ile görüntü okuma, gösterme ve kaydetme

Renk uzayları (BGR, RGB, HSV, Grayscale)

Piksel manipülasyonu (parlaklık/kontrast)

Temel çizim fonksiyonları

Klavye ve fare etkileşimleri

Yeniden boyutlandırma, döndürme, kırpma

Görselleri birleştirme (kolaj oluşturma)

🖼️ Çıktılar

Her çalıştırılan dosya, sonuç görselini outputs/ klasörüne kaydeder.

Kolaj uygulamasında çıktı: outputs/collage_out.jpg

Diğer dosyalar test amaçlı yeni görseller oluşturabilir.

⚠️ Notlar

Proje dizininde Türkçe karakter (örnek: “Masaüstü”) bulunmamalıdır.

Görsellerin isimleri kodla birebir aynı olmalıdır.

Tüm işlemler os.path yöntemiyle platformdan bağımsız hale getirilmiştir.