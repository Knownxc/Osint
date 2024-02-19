import json

with open('../Osint/modules/Resources/data.json') as f:
    site_list = json.load(f)

def get_site_list():
    return site_list

def get_profile_link(site):
    return site_list[site]['Profile']

def get_name():
    return [name for name in site_list]

def get_error(site):
    site_list = get_site_list()
    return site_list[site]['Error']

def get_title_search(site):
    site_list = get_site_list()
    return site_list[site]['Title']
