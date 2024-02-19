import requests
from bs4 import BeautifulSoup
from .library.list import *

def profile_links(input_url):
    profile_links = {}
    names = get_name()
    for name in names:
        profile_links[name] = get_profile_link(name).format(url=input_url)
    return profile_links

def check_profile(input):
    for site, link in input.items():
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tags = soup.find_all('title')
        check_error = get_error(site)
        if title_tags == [] or any(check_error in tag.text.strip() for tag in title_tags):
            print(f"{site} - No Profile Found!")
            print(title_tags)
        else:
            print(f"{site} - Profile Found: {link}")
