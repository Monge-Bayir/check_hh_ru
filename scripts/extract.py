import json
from datetime import datetime
import os

import requests


def extract_data():
    query = {"text": "Data Engineer", "area": 1, "per_page": 50}
    res = requests.get('https://api.hh.ru/vacancies', params=query)
    data = res.json()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    with open(f'../data/unrefined/hh_unrefined_{timestamp}.json', 'w') as file:
        json.dump(data['items'], file)

    return data['items']

