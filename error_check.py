import requests
from bs4 import BeautifulSoup

def get_profile(input):
    url = f'https://instagram.com/{input}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('title').text
    if name == "Instagram":
        return "No Profile Found!"
    return name

print(get_profile('selenagomez'))