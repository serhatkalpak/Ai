from transformers import pipeline

def run():
    model = pipeline("sentiment-analysis")
    text = input("Metin: ")
    result = model(text)[0]
    print(f"Duygu: {result['label']}, Skor: {result['score']:.2f}")