import yfinance as yf

def calistir():
    veri = yf.download("USDTRY=X", period="1d")
    print(f"💰 Güncel USD/TRY: {veri['Close'][-1]:.2f}")