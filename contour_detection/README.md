# KONTUR ALGILAMA VE ANALİZİ

## 1. Proje Hakkında
Bu proje, dijital bir görüntüdeki nesneleri (örneğin meyveleri) otomatik olarak tespit etmek, saymak ve numaralandırmak amacıyla hazırlanmıştır.  
Projede **Canny kenar tespiti** ve **kontur analizi** yöntemleri kullanılmıştır.  
Kullanıcı, **TrackBar** yardımıyla kenar tespiti için kullanılan eşik değerlerini değiştirebilir ve sonuçları anlık olarak ekranda görebilir.

---

## 2. Projenin Amacı
Projenin amacı, görüntü işleme yöntemlerini kullanarak bir görüntüdeki nesneleri otomatik olarak bulmak ve analiz etmektir.  
Kontur bulma, kenar tespiti, nesne sayımı ve şekil analizi gibi temel işlemler uygulamalı olarak öğrenilmiştir.

---

## 3. Kullanılan Yöntemler ve Teknikler
- **Canny Kenar Tespiti:** Görüntüdeki nesnelerin net sınırlarını belirlemek için kullanılmıştır.  
- **Kontur Bulma:** `cv2.findContours()` fonksiyonu ile nesnelerin dış hatları tespit edilmiştir.  
- **Kontur Özellikleri:** Alan, merkez ve çevre gibi temel özellikler incelenmiştir.  
- **Morfolojik Closing İşlemi:** Açık veya bölünmüş şekillerin kenarlarını birleştirip tek nesne olarak algılanmasını sağlamak için eklenmiştir.  
- **TrackBar Kullanımı:** Kullanıcıya Canny kenar eşiğini dinamik olarak değiştirme imkânı sunulmuştur.

---

## 4. Proje Yapısı
contour_detection/
│
├── assets/
│ └── input.jpg # Girdi görseli
│
├── outputs/
│ └── result.jpg # İşlenmiş çıktı görseli
│
├── src/
│ └── main.py # Ana Python dosyası
│
├── README.md # Proje açıklama dosyası
└── requirements.txt # Gerekli kütüphaneler

yaml
Kodu kopyala

---

## 5. Nasıl Çalıştırılır

### Gerekli kütüphaneleri yükle:
```bash
pip install -r requirements.txt
Uygulamayı başlat:
bash
Kodu kopyala
cd contour_detection/src
python main.py
Kullanım:
Açılan pencerede TrackBar’lar ile Canny eşik değerlerini değiştir.

Ekranın sağında nesnelerin konturları çizilmiş, numaraları yazılmış halini görürsün.

Sol tarafta kenar tespiti sonucu gösterilir.

ESC tuşuna basarak programdan çıkabilirsin.

Çıkış yapıldığında sonuç görseli outputs/result.jpg olarak kaydedilir.

6. Beklenen Sonuç
Program çalıştırıldığında:

Görüntüdeki nesneler tespit edilir.

Her nesnenin sınırları çizilir.

Her nesneye bir numara atanır.

Toplam nesne sayısı ekranda görüntülenir.

