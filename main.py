import importlib
import subprocess
import sys

MODULES = {
    "1": {"name": "Web Analizi", "libs": ["requests", "beautifulsoup4"], "module": "web_analyzer"},
    "2": {"name": "Duygu Analizi", "libs": ["transformers"], "module": "sentiment_analysis"},
    "3": {"name": "Müzik Oluştur", "libs": ["midiutil"], "module": "music_generator"},
    "4": {"name": "Döviz Analizi", "libs": ["yfinance"], "module": "currency_analyzer"},
    "5": {"name": "Ürün Karşılaştır", "libs": ["requests"], "module": "price_comparator"},
    "6": {"name": "AI Fotoğraf", "libs": ["pillow"], "module": "image_creator"},
    "7": {"name": "Maç Tahmini", "libs": ["scikit-learn"], "module": "match_predictor"},
    "8": {"name": "Konum Bul", "libs": ["geopy"], "module": "location_finder"}
}

def check_and_install(libs):
    for lib in libs:
        try:
            importlib.import_module(lib)
            print(f"✅ {lib} zaten yüklü!")
        except ImportError:
            print(f"⏳ {lib} yükleniyor...")
            subprocess.run(f"pip install {lib}", shell=True, check=True)

def main():
    while True:
        print("\n🤖 Termux AI Araç Kutusu")
        for key, val in MODULES.items():
            print(f"{key}- {val['name']}")
        print("q- Çıkış")
        
        secim = input("Seçim: ")
        if secim == "q":
            break
        elif secim in MODULES:
            modul = MODULES[secim]
            check_and_install(modul["libs"])
            try:
                module = importlib.import_module(f"modules.{modul['module']}")
                module.run()
            except Exception as e:
                print(f"❌ Hata: {e}")
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()