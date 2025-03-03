from transformers import pipeline

def run():
    model = pipeline("sentiment-analysis")
    text = input("Metin girin: ")
    result = model(text)[0]
    print(f"Duygu: {result['label']}, Skor: {result['score']:.2f}")