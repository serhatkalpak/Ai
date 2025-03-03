import requests

def run():
    url = input("URL girin: ")
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")