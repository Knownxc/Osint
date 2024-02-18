import json

with open('../Osint/modules/data.json') as f:
    site_list = json.load(f)

def get_site_list():
    return site_list

def get_profile_link(site):
    return site_list[site]['Profile']
