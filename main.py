import os
import sys
import subprocess
import importlib

MODULLER = {
    "1": {"ad": "🕸️ Web Analizi", "kutuphaneler": ["requests", "beautifulsoup4"], "modul": "web_analizi"},
    "2": {"ad": "😃 Duygu Analizi", "kutuphaneler": ["transformers"], "modul": "duygu_analizi"},
    "3": {"ad": "🎵 Müzik Oluştur", "kutuphaneler": ["midiutil"], "modul": "muzik_olustur"},
    "4": {"ad": "💵 Döviz Analizi", "kutuphaneler": ["yfinance"], "modul": "doviz_analiz"},
    "5": {"ad": "🛒 Ürün Karşılaştır", "kutuphaneler": ["requests"], "modul": "urun_karsilastir"},
    "6": {"ad": "🎨 Resim Oluştur", "kutuphaneler": ["pillow"], "modul": "resim_olustur"},
    "7": {"ad": "⚽ Maç Tahmini", "kutuphaneler": ["scikit-learn"], "modul": "mac_tahmin"},
    "8": {"ad": "📍 Konum Bul", "kutuphaneler": ["geopy"], "modul": "konum_bul"},
    "9": {"ad": "📜 Şiir Yaz", "kutuphaneler": ["transformers"], "modul": "siir_yaz"},
    "10": {"ad": "📚 Kitap Yaz", "kutuphaneler": ["transformers"], "modul": "kitap_yaz"},
    "g": {"ad": "🔄 Güncelle", "modul": "guncelle"}
}

def kutuphane_kontrol(kutuphaneler):
    for lib in kutuphaneler:
        try:
            importlib.import_module(lib)
            print(f"✅ {lib} zaten yüklü!")
        except ImportError:
            print(f"⏳ {lib} yükleniyor...")
            subprocess.run(f"pip install {lib}", shell=True, check=True)

def guncelle():
    print("\n" + "="*30)
    print("GÜNCELLEME BAŞLATILIYOR...")
    subprocess.run("git pull origin main", shell=True, check=True)
    subprocess.run("pip install -r requirements.txt --upgrade", shell=True)
    print("✅ Güncelleme tamamlandı! Komut satırını yeniden başlatın.")

def ana_menu():
    while True:
        print("\n" + "="*30)
        print("🤖 TERMUX AI ARAÇ KUTUSU")
        for key, value in MODULLER.items():
            if key != "g":
                print(f"{key}- {value['ad']}")
        print("g- Güncelle")
        print("q- Çıkış")
        
        secim = input("Seçiminiz: ").lower()
        
        if secim == "q":
            break
        elif secim == "g":
            guncelle()
        elif secim in MODULLER:
            secilen = MODULLER[secim]
            if "kutuphaneler" in secilen:
                kutuphane_kontrol(secilen["kutuphaneler"])
            modul = importlib.import_module(secilen["modul"])
            modul.calistir()
        else:
            print("❌ Geçersiz seçim!")

if __name__ == "__main__":
    ana_menu()