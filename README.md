🛒 Trendyol Ürün Takip ve Analiz Sistemi
Bu proje, Trendyol'dan bilgisayar ürünlerini çekerek analiz eden, veritabanına kaydeden ve raporlayan otomatik bir web scraping ve veri analizi uygulamasıdır.

🚀 Özellikler
🌐 Web Scraping
Trendyol'dan Ürün Çekme: "pc" aramasıyla 6 bilgisayar ürünü

Otomatik Çerez Yönetimi: Çerez bildirimini kapatma

Ürün İsmi ve Fiyat: Selenium ile dinamik veri çekme

📊 Veri Analizi
Ortalama fiyat hesaplama

En pahalı ve en ucuz ürün tespiti

Fiyat kategorizasyonu (Ucuz/Normal/Pahalı)

CSV formatında dışa aktarma

💾 Veritabanı İşlemleri (MySQL)
Veri kaydetme

Verileri listeleme

Veri güncelleme

Veri silme

📈 Grafik ve Raporlama
Bar Grafiği: Ürün-fiyat karşılaştırması

Pasta Grafiği: Fiyat dağılımı analizi

İleri Düzey Analiz: Histogram + KDE yoğunluk eğrisi

PDF Raporu: Tüm grafikler PDF olarak kaydedilebilir

📁 Gereksinimler
bash
pip install mysql-connector-python scipy pandas numpy matplotlib reportlab selenium
🔧 Kurulum
Projeyi klonlayın

MySQL veritabanı oluşturun:

sql
CREATE DATABASE trendyol;
USE trendyol;
CREATE TABLE bilgisayarlar (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    İsim VARCHAR(255),
    Fiyat DECIMAL(10,2),
    Kategori VARCHAR(100),
    Durum VARCHAR(50)
);
Kodda MySQL bağlantı bilgilerini güncelleyin

Microsoft Edge WebDriver'ı yükleyin

Programı çalıştırın:

bash
python trendyol_analysis.py
📂 Dosya Yapısı
trendyol_analysis.py - Ana program dosyası

hata_dosyam.text - Hata loglama dosyası

trendyol.csv - Analiz sonuçları CSV dosyası

*.png - Oluşturulan grafik dosyaları

*.pdf - Oluşturulan PDF raporları

🎯 Kullanım
Program çalıştırıldığında ana menü karşınıza gelir:

text
****** TRENDYOL ÜRÜN TAKİP SİSTEMİNE HOŞGELDİNİZ! 🥰 ******
YAPABİLECEKLERİNİZ:
1=Trendyol'dan ürün çekme 🛒
2=Ürünlerin Analizi 🧠
3=Veritabanına Kayıt
4=Grafik ve Rapor Oluşturma 📊
5=Sistemden Çıkış 🥲
📝 Menü Detayları
1. Ürün Çekme

Trendyol'da "pc" araması yapar

6 farklı bilgisayar ürününün isim ve fiyatını çeker

2. Ürün Analizi

Ortalama fiyat hesaplama

En pahalı/ucuz ürün tespiti

Fiyat durumu kategorizasyonu

CSV kaydı

3. Veritabanı İşlemleri

Veri kaydetme

Verileri listeleme

ID ile veri güncelleme

ID ile veri silme

4. Grafik ve Rapor

3 farklı grafik türü

PDF raporu oluşturma

📊 Grafik Türleri
Bar Grafiği
Ürün isimleri ve fiyatları

Kırmızı barlar, sarı kenarlık

PDF rapor desteği

Pasta Grafiği
Fiyat dağılımı

6 farklı renk

Gölge efektli

PDF rapor desteği

İleri Düzey Analiz
Histogram (8 bins)

KDE (Kernel Density Estimation) yoğunluk eğrisi

Siyah kesikli çizgi ile yoğunluk gösterimi

PDF rapor desteği

📄 PDF Raporları
Her grafik için PDF raporu özellikleri:

Grafik görseli

Başlık

Açıklama metni

Oluşturulma zamanı

💾 Veritabanı Şeması
Tablo: bilgisayarlar

Id INT AUTO_INCREMENT PRIMARY KEY

İsim VARCHAR(255)

Fiyat DECIMAL(10,2)

Kategori VARCHAR(100)

Durum VARCHAR(50)

📈 Fiyat Kategorizasyonu
Ucuz: 10.000 TL altı

Normal: 10.000 - 20.000 TL arası

Pahalı: 20.000 TL üstü

⚠️ Hata Yönetimi
Tüm hatalar hata_dosyam.text dosyasına kaydedilir:

Hata mesajı

Zaman damgası

Kullanıcıya uygun mesaj gösterimi

🔧 Teknolojiler
Web Scraping: Selenium WebDriver

Veri Analizi: Pandas, NumPy, SciPy

Grafik: Matplotlib

Veritabanı: MySQL Connector

Raporlama: ReportLab

İstatistik: Gaussian KDE

🌐 Web Scraping Detayları
URL: https://www.trendyol.com/

Arama: "pc"

Bekleme: WebDriverWait ile dinamik yükleme

Veri Temizleme: TL simgesi, nokta ve virgül temizliği

⚙️ Teknik Özellikler
Otomatik çerez bildirimi yönetimi

Dinamik XPath kullanımı

Veri tipi dönüşümleri

Exception handling

Loglama sistemi
