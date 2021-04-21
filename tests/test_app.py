'''Basic test script to test whether connection is getting established'''

import json
import requests
from flask import json

def test_index():
    data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female","HeightCm": 167, "WeightKg": 82}]
    r = requests.post("http://127.0.0.1:5000/", json = data)

    #status code 200 implies successfull response
    assert r.status_code == 200
