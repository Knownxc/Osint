import requests
from bs4 import BeautifulSoup
from library.list import *

def Site_cycle():
    names = get_name()
    for name in names:
        print(get_profile_link(name))
    
