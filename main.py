from web_analyzer import run
import importlib
import subprocess

MODULES = {
    "1": {"name": "Web Analizi", "libs": ["requests"], "module": "web_analyzer"},
    "2": {"name": "Duygu Analizi", "libs": ["transformers"], "module": "sentiment_analysis"}
}

def check_install(libs):
    for lib in libs:
        try:
            importlib.import_module(lib)
        except ImportError:
            subprocess.run(f"pip install {lib}", shell=True)

def main():
    while True:
        print("\n🤖 Termux AI Araç Kutusu")
        for key, val in MODULES.items():
            print(f"{key}- {val['name']}")
        choice = input("Seçim: ")
        
        if choice == "q":
            break
        elif choice in MODULES:
            mod = MODULES[choice]
            check_install(mod["libs"])
            module = importlib.import_module(mod["module"])
            module.run()
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main()