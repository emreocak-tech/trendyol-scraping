import mysql.connector
from scipy.stats import gaussian_kde
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from reportlab.lib.utils import ImageReader
plt.style.use("seaborn-v0_8-darkgrid")
ürünler=[]
ürünlerin_fiyatı=[]
def logla(mesaj):
    with open("hata_dosyam.text","a+",encoding="utf-8") as file:
        file.write("\n" + " " + "HATA : " + " " + mesaj + " " + "Zaman : " + " " + str(datetime.datetime.now()))
def ürün_al():
    url = "https://www.trendyol.com/"
    driver = webdriver.Edge()
    driver.get(url=url)
    driver.maximize_window()
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-reject-all-handler"]'))).click()
    except:
        print("Çerez bulunamadı veya önceden kaydedilmiş")
    arama_kutusu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, '//input[@placeholder="Aradığınız ürün, kategori veya markayı yazınız"]')))
    arama_kutusu.send_keys("pc")
    arama_kutusu.send_keys(Keys.ENTER)
    #time.sleep(100000000)
    ürün_ismi = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[1]/a/div[2]/div[1]/div[1]/div/h3/span[2]')))
    ürün_fiyat = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[1]/a/div[2]/div[1]/div[4]/div[2]/div[1]/div')))
    yeni_ürün_fiyat = ürün_fiyat.text.replace("TL", " ").replace(".", "").replace(",", ".").strip()
    ürün_ismi2=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[3]/a/div[2]/div[1]/div[1]/div/h3/span[2]')))
    ürün_fiyat2=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[3]/a/div[2]/div[1]/div[4]/div[2]/div[1]/div/div')))
    yeni_ürün_fiyat2=ürün_fiyat2.text.replace("TL"," " ).replace(".","").replace(",",".").strip()
    ürün_ismi3=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[5]/a/div[2]/div[1]/div[1]/div/h3/span[2]')))
    ürün_fiyat3=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[5]/a/div[2]/div[1]/div[4]/div[2]/div[1]/div/div')))
    yeni_ürün_fiyat3=ürün_fiyat3.text.replace("TL", " ").replace(".", "").replace(",", ".").strip()
    ürün_ismi4=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[25]/a/div[2]/div[1]/div[1]/div/h3/span[2]')))
    ürün_fiyatı4=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[25]/a/div[2]/div[1]/div[4]/div[2]/div[1]/div/div')))
    ürün_ismi5=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[27]/a/div[2]/div[1]/div[1]/div/h3/span[2]')))
    ürün_fiyatı5=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[27]/a/div[2]/div[1]/div[4]/div[2]/div[1]/div[2]')))
    ürün_ismi6=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[31]/a/div[2]/div[1]/div[1]/div/h3/span[2]')))
    ürün_fiyatı6=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="search-app"]/div/div/div/div[2]/div[4]/div[1]/div/div[31]/a/div[2]/div[1]/div[4]/div[2]/div[1]/div[2]')))
    yeni_ürün_fiyat4=ürün_ismi4.text.replace("TL", " ").replace(".", "").replace(",", ".").strip()
    yeni_ürün_fiyat5=ürün_fiyatı5.text.replace("TL", " ").replace(".", "").replace(",", ".").strip()
    yeni_ürün_fiyat6=ürün_fiyatı6.text.replace("TL", " ").replace(".", "").replace(",", ".").strip()
    print(f"ÜRÜNLER : {ürün_ismi} , {ürün_ismi2},  , {ürün_ismi5} , {ürün_ismi6} , {ürün_ismi4} , {ürün_ismi3}")
    ürünler.append(ürün_ismi.text)
    ürünler.append(ürün_ismi2.text)
    ürünler.append(ürün_ismi3.text)
    ürünler.append(ürün_ismi4.text)
    ürünler.append(ürün_ismi5.text)
    ürünler.append(ürün_ismi6.text)
    ürünlerin_fiyatı.append(yeni_ürün_fiyat)
    ürünlerin_fiyatı.append(yeni_ürün_fiyat2)
    ürünlerin_fiyatı.append(yeni_ürün_fiyat3)
    ürünlerin_fiyatı.append(yeni_ürün_fiyat4)
    ürünlerin_fiyatı.append(yeni_ürün_fiyat5)
    ürünlerin_fiyatı.append(yeni_ürün_fiyat6)
    driver.quit()
def analiz_yap():
    df=pd.DataFrame({"ÜRÜN":ürünler , "ÜRÜNLERİN FİYATI":ürünlerin_fiyatı , "ÜRÜNLERİN KATEGORİSİ":"BİLGİSAYAR"},index=range(1,len(ürünler)+1))
    ortalama=df["ÜRÜNLERİN FİYATI"].mean(only_numeric=True)
    en_yüksek_değer=df.nlargest(1,"ÜRÜNLERİN FİYATI")[["ÜRÜN","ÜRÜNLERİN FİYATI"]]
    en_düşük_değer=df.nsmallest(1,"ÜRÜNLERİN FİYATI")[["ÜRÜN","ÜRÜNLERİN FİYATI"]]
    print(f"DEĞERİ EN YÜKSEK OLAN BİLGİSAYAR : {en_yüksek_değer['ÜRÜN'].values} , BİLGİSAYARIN FİYATI : {en_yüksek_değer['ÜRÜNLERİN FİYATI'].values}")
    print(f"DEĞERİ EN DÜŞÜK OLAN BİLGİSAYAR : {en_düşük_değer['ÜRÜN'].values} , BİLGİSAYARIN FİYATI : {en_düşük_değer['ÜRÜNLERİN FİYATI'].values}")
    print(F"ÜRÜNLERİN ORTALAMA FİYAT DEĞERİ : {ortalama} TL'DİR.")
    def fonksiyon_ekle(fiyat):
        if fiyat>20000:
            return "PAHALI"
        elif 10000<=fiyat<=20000:
            return "NORMAl"
        elif 10000<fiyat:
            return "UCUZ"
    df["FİYAT DURUMUNA GÖRE UCUZLUK-PAHALILIK DURUMU"]=df["ÜRÜNLERİN FİYATI"].apply(fonksiyon_ekle)
    df.to_csv("trendyol.csv",encoding="utf-8-sig")
    print("DataFrame csv dosyasına çevrildi!")
def veri_tabanına_kaydet():
    conn=mysql.connector.connect("KULLANICI KENDİ BİLGİLERİNİ GİRMELİDİR!")
    cursor=conn.cursor()
    print("VERİTABANI FONKSİYONUNA HOŞGELDİNİZ")
    print("YAPABİLECEKLERİNİZ:\n1=Verileri Kaydetme⏺️\n2=Veritabanındaki Verileri Terminale Yazdırma\n3=Veri Güncelleme\n4=Veri Silme")
    try:
        karar=int(input("Yapmak İstediğiniz İşlemi Seçiniz : "))
        if karar==1:
            sql_sorgum1 = "INSERT INTO bilgisayarlar(İsim,Fiyat,Kategori,Durum) VALUES (%s,%s,%s,%s)"
            values1 = (ürünler[0], ürünlerin_fiyatı[0], "BİLGİSAYAR", "Bilinmiyor")
            sql_sorgum2 = "INSERT INTO bilgisayarlar(İsim,Fiyat,Kategori,Durum) VALUES (%s,%s,%s,%s)"
            values2 = (ürünler[1], ürünlerin_fiyatı[1], "BİLGİSAYAR", "Bilinmiyor")
            sql_sorgum3 = "INSERT INTO bilgisayarlar(İsim,Fiyat,Kategori,Durum) VALUES (%s,%s,%s,%s)"
            values3 = (ürünler[2], ürünlerin_fiyatı[2], str("BİLGİSAYAR"), str("Bilinmiyor"))
            sql_sorgum4 = "INSERT INTO bilgisayarlar(İsim,Fiyat,Kategori,Durum) VALUES (%s,%s,%s,%s)"
            values4 = (ürünler[3], ürünlerin_fiyatı[3], "BİLGİSAYAR", "Bilinmiyor")
            sql_sorgum5 = "INSERT INTO bilgisayarlar(İsim,Fiyat,Kategori,Durum) VALUES (%s,%s,%s,%s)"
            values5 = (ürünler[4], ürünlerin_fiyatı[4], "BİLGİSAYAR", "Bilinmiyor")
            sql_sorgum6 = "INSERT INTO bilgisayarlar(İsim,Fiyat,Kategori,Durum) VALUES (%s,%s,%s,%s)"
            values6 = (ürünler[5], ürünlerin_fiyatı[5], "BİLGİSAYAR", "Bilinmiyor")
            cursor.execute(sql_sorgum1, values1)
            cursor.execute(sql_sorgum2, values2)
            cursor.execute(sql_sorgum3, values3)
            cursor.execute(sql_sorgum4, values4)
            cursor.execute(sql_sorgum5, values5)
            cursor.execute(sql_sorgum6, values6)
            print("BÜTÜN VERİLER KAYDEDİLDİ.")
            conn.commit()
            conn.close()
        elif karar==2:
            sql_sorgum7="SELECT * FROM bilgisayarlar"
            cursor.execute(sql_sorgum7)
            veri=cursor.fetchall()
            for veriler in veri:
                print(veriler)
            conn.commit()
            conn.close()
        elif karar==3:
            sql_sorgum8="UPDATE bilgisayarlar SET İsim=%s WHERE Id=%s"
            try:
               ıd_al=int(input("DEĞİŞTİRMEK İSTEDİĞİNİZ VERİNİN ID NUMARASINI GİRİNİZ : "))
            except ValueError as v:
                print(f"HATA : {v} , LÜTFEN ID DEĞERİNİ GİRİN")
            except:
                print("BELİRTİLEN ID DEĞERİNE ULAŞILAMADI❗ ")
            cursor.execute(sql_sorgum8,ıd_al)
            conn.commit()
        elif karar==4:
            sql_sorgum9="DELETE FROM bilgisayarlar  WHERE Id=%s"
            ıd_al2=int(input("Silmek istediğiniz verinin ıd numarasını giriniz : "))
            cursor.execute(sql_sorgum9,ıd_al2)
            conn.commit()
            conn.close()
        else:
            print("Lütfen Belirtilen Değerleri Tuşlayınız😤")
            logla("Kullanıcı Belirtilen Değerleri Girmedi")
    except ValueError as v:
        print(f"Lütfen Belirtilen Değerleri Tuşlayınız😤 ,Hata Kodu : {v}")
        logla("Kullanıcı Belirtilen Değerleri Girmedi")
def grafik_çiz():
    print("GRAFİK ÇİZME FONKSİYONUNA HOŞGELDİNİZ📈".center(50,"*"))
    print("YAPABİLECEKLERİNİZ:\n1=Bar Grafiği📉\n2=Pasta Grafiği📊\n3=İleri Düzey Analiz🧾")
    try:
        decision=int(input("Yapmak İstediğiniz İşlemi Giriniz : "))
        if decision==1:
            plt.bar(ürünler,ürünlerin_fiyatı,color="Red",edgecolor="Yellow",linewidth=3)
            plt.xlabel("ÜRÜNLERİN İSİMLERİ",color="Black",fontsize=15)
            plt.ylabel("FİYAT DEĞERLERİ",color="Black",fontsize=15)
            plt.title("ÜRÜN-FİYAT İLİŞKİSİ",color="Black",fontsize=20)
            plt.grid(True)
            plt_filename="bar_grafiği.png"
            plt.savefig(plt_filename, dpi=300, bbox_inches='tight')
            try:
                karar=int(input("Grafiği PDF dosyası şeklinde istiyorsanız 1 , istemiyorsanız 0 tuşlayınız"))
                if karar==1:
                    pdf_filename="rapor1.pdf"
                    c=canvas.Canvas(pdf_filename)
                    c.setFont("Times-Roman",16)
                    c.drawString(150,792,"ÜRÜNLERE GÖRE BAR GRAFİĞİ")
                    img=ImageReader(plt_filename)
                    img_width, img_height = 400, 200
                    c.drawImage(img, 100, 500, width=img_width, height=img_height)
                    c.setFont("Helvetica", 12)
                    c.drawString(25, 400, "BU GRAFIK ÜRÜN-FİYAT İLİŞKİSİNİ BAR GRAFİĞİ İLE İNCELER")
                    c.setFont("Helvetica", 12)
                    c.drawString(0, 250, f"BU DOSYANIN OLUSTURULMA ZAMANI {datetime.datetime.now()}")
                    c.save()
                elif karar==0:
                    print("Matplotlib kütüphanesi hazırlanıyor...")
                    time.sleep(3)
                    plt.show()
                else:
                    print("Lütfen Belirtilen Değerleri Tuşlayınız!")
                    logla("Kullanıcı Belirtilen Değerleri Girmedi")
            except ValueError as ert:
                print(f"Hata Kodu : {ert} , Lütfen Belirtilen Değerleri Tuşlayınız")
                logla("Kullanıcı Belirtilen Değerleri Girmedi")
        elif decision==2:
            plt.pie(ürünlerin_fiyatı,labels=ürünler,colors=["Black","Blue","Yellow","Red","Purple","Orange"],shadow=True)
            plt.title("FİYAT-ÜRÜN İLİŞKİSİNİN PASTA GRAFİĞİ İLE İNCELENMESİ",color="Black",fontsize=20)
            plt_filename="pasta_grafiği.png"
            plt.savefig(plt_filename,dpi=300, bbox_inches='tight')
            try:
                karar=int(input("Grafiği PDF dosyası şeklinde istiyorsanız 1 , istemiyorsanız 0 tuşlayınız"))
                if karar==1:
                    pdf_filename="pasta_grafiği.pdf"
                    c=canvas.Canvas(pdf_filename)
                    c.setFont("Times-Roman",16)
                    c.drawString(150,792,"Pasta Grafiği ile Ürün-Fiyat Analizi")
                    ımg=ImageReader(plt_filename)
                    img_width, img_height = 400, 200
                    c.drawImage(ımg, 100, 500, width=img_width, height=img_height)
                    c.setFont("Helvetica", 12)
                    c.drawString(25, 400, "BU GRAFIK ÜRÜN-FİYAT İLİŞKİSİNİ PASTA GRAFİĞİ İLE İNCELER")
                    c.setFont("Helvetica", 12)
                    c.drawString(0, 250, f"BU DOSYANIN OLUSTURULMA ZAMANI {datetime.datetime.now()}")
                    c.save()
                elif karar==0:
                    print("Matplotlib kütüphanesi hazırlanıyor...")
                    plt.show()
                else:
                    print("Lütfen Belirtilen Değerleri Tuşlayınız")
                    logla("Kullanıcı Belirtilen Değerleri Girmedi")
            except ValueError as v:
                print(f"Hata Kodu : {v} , Lütfen Belirtilen Değerleri Tuşlayınız")
                logla("Kullanıcı Belirtilen Değerleri Girmedi")
        elif decision==3:
            plt.hist(ürünlerin_fiyatı,bins=8,density=True,color="Yellow",edgecolor="Red",linewidth=3)
            kde=gaussian_kde(ürünlerin_fiyatı)
            x=np.linspace(min(ürünlerin_fiyatı),max(ürünlerin_fiyatı),100)
            plt.plot(x,kde(x),color="Black",label="Yoğunlaşma Eğrisi",linewidth=3,linestyle=":")
            plt.title("İLERİ DÜZEY ANALİZ",fontsize=20,color="Black")
            plt.legend()
            plt.grid(True)
            plt_filename="ileri_düzey.png"
            plt.savefig(plt_filename,dpi=300, bbox_inches='tight')
            try:
                karar=int(input("Grafiği PDF şeklinde istiyorsanız 1 , istemiyorsanız 0 giriniz : "))
                if karar==1:
                    pdf_filename="ileri_düzey.pdf"
                    c=canvas.Canvas(pdf_filename)
                    c.setFont("Times-Roman",16)
                    c.drawString(150,792,"KDE ANALİZ")
                    ımg=ImageReader(plt_filename)
                    c.drawImage(ımg,100,750,width=400,height=200)
                    c.drawString(25, 400, "BU GRAFIK KDE İLE ÜRÜN-FİYAT İLŞKİSİNİ İNCELER")
                    c.setFont("Helvetica", 12)
                    c.drawString(0, 250, f"BU DOSYANIN OLUSTURULMA ZAMANI {datetime.datetime.now()}")
                    c.save()
                elif karar==0:
                    print("Matplotlib kütüphanesi hazırlanıyor...")
                    time.sleep(3)
                    plt.show()
                else:
                    print("Lütfen Belirtilen Değerleri Tuşlayınız")
                    logla("Kullanıcı Belirtilen Değerleri Girmedi")
            except ValueError as ghj:
                print(f"Hata Kodu : {ghj} , Lütfen Belirtilen Değerleri Tuşlayınız")
                logla("Kullanıcı Belirtilen Değerleri Girmedi")
    except ValueError as qwe:
        print(f"Hata Kodu:{qwe} , Lütfen Belirtilen Değerleri Giriniz ❗")
        logla("Kullanıcı Belirtilen Değerleri Girmedi")
def main():
    print("TRENDYOL ÜRÜN TAKİP SİSTEMİNE HOŞGELDİNİZ!🥰".center(50,"*"))
    print("YAPABİLECEKLERİNİZ:\n1=Trendyol'dan ürün çekme🛒\n2=Ürünlerin Analizi🧠\n3=Veritabanına Kayıt\n4=Grafik ve Rapor Oluşturma📊\n5=Sistemden Çıkış🥲")
    while True:
        try:
            karar = int(input("Yapmak istediğiniz işlemin numarasını giriniz : "))
            if karar == 1:
                ürün_al()
            elif karar == 2:
                ürün_al()
                analiz_yap()
            elif karar == 3:
                ürün_al()
                veri_tabanına_kaydet()
            elif karar == 4:
                ürün_al()
                grafik_çiz()
            elif karar == 5:
                print("SİSTEMDEN ÇIKILIYOR...")
                time.sleep(3)
                print("Sistemden Çıkıldı")
                quit()
            else:
                print("Lütfen Belirtilen Değerleri Giriniz😤")
                logla("Kullanıcı Belirtilen Değerleri Girmedi")
        except ValueError as v:
           print(f"Lütfen Belirtilen Değerleri Girin!😤, Hata Kodu {v}❗")
           logla("Kullanıcı Belirtilen Değerleri Girmedi")
        finally:
            print("Sistem Düzgün Çalışıyor✔️")
if __name__ == "__main__":
    main()




































































































































































