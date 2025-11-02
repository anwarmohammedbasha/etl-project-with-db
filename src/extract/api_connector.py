"""
api_connector.py — Template for future API integrations
"""
import requests

def fetch_api_data(endpoint: str, params=None):
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()
