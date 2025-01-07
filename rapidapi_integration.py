import requests
import os

API_KEY = os.getenv("RAPIDAPI_KEY")

def fetch_fund_data(family):
    url = "https://latest-mutual-fund-nav.p.rapidapi.com/fetchOpenEndFunds"
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "latest-mutual-fund-nav.p.rapidapi.com"
    }
    params = {"family": family}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return None






