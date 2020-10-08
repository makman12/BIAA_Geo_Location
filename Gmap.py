import requests
from urllib.parse import urlencode
import pandas as pd
import time
api_key="AIzaSyCB6W4sBmDeSDgbtCzqJs7Zn6JYuVdQbzo"
def gmap(address_or_postalcode, data_type = 'json'):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": address_or_postalcode, "key": api_key}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    if r.status_code not in range(200, 299):
        return {}
    latlng = {}
    adress={}
    cevap=["","",""]
    try:
        all=r.json()['results']
        latlng = r.json()['results'][0]['geometry']['location']
        adress = r.json ()['results'][0]['formatted_address']
        cevap = [latlng.get ("lat"), latlng.get ("lng"), adress]
    except:
        pass
    return cevap

