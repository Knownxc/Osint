import requests
from bs4 import BeautifulSoup
from library.list import *

def construct_profile_links(input_url):
    profile_links = {}
    names = get_name()
    for name in names:
        profile_links[name] = get_profile_link(name).format(url=input_url)
    return profile_links

def check_profile(input):
    for site, link in input.items():
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find('title')
        if title_tag is None or title_tag.text == get_error(site):
            print(f"{site} - No Profile Found!")
        else:
            print(f"{site} - Profile Found: {link}")

input_url = input("Enter the URL: ")
links = construct_profile_links(input_url)
check_profile(links)
