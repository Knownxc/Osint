import requests
from bs4 import BeautifulSoup

def get_profile(input):
    url = f'https://youtube.com/@{input}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('title')
    if name == "None":
        return "No Profile Found!"
    return name

print(get_profile('Hydra8270'))