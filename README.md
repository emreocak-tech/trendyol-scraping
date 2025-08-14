README_TR.md  (Türkçe)

# Trendyol Ürün Takip Sistemi

[Trendyol](https://www.trendyol.com) sitesinden bilgisayar fiyatlarını otomatik çeken, MySQL’e kaydeden, temel analizler yapan ve grafik + PDF raporu oluşturan Python tabanlı bir projedir.

## Özellikler
- **Selenium** ile Edge tarayıcı üzerinden web scraping  
- Fiyat temizliği (₺, nokta, virgül düzenlemeleri)  
- **Pandas** ile analiz: ortalama, en pahalı/ucuz ürün  
- **Matplotlib** görselleri: çubuk, pasta, KDE histogram  
- **ReportLab** ile PDF raporlama  
- MySQL CRUD işlemleri (ekleme, listeleme, güncelleme, silme)  
- Türkçe/İngilizce CLI menüsü


# Trendyol Scraper & Analyzer

A lightweight Python project that automatically scrapes computer prices from [Trendyol](https://www.trendyol.com), stores them in a MySQL database, performs basic analytics, and produces charts plus PDF reports.

## Features
- Web scraping with **Selenium** (Edge driver).
- Data cleaning & price conversion (₺ → float).
- **Pandas** analysis: mean, min, max, custom price buckets.
- **Matplotlib** visualizations:
  - Bar chart, pie chart, KDE histogram.
- **ReportLab** PDF export.
- MySQL persistence with CRUD options.
- Dual-language CLI prompts (EN / TR).
