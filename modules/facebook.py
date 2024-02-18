import requests
from bs4 import BeautifulSoup

def get_facebook_profile(input):
    url = f'https://facebook.com/{input}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find('title').text
    if name == "Facebook":
        return "No Profile Found!"
    return name

print(get_facebook_profile('sdkjfhsdkjhfs'))
