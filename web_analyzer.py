import requests
from bs4 import BeautifulSoup

def run():
    url = input("URL girin: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Başlık: {soup.title.text}")