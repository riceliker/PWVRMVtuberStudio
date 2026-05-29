import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def getPort():
    print(os.path.join(BASE_DIR, "../config.json"))
    with open(os.path.join(BASE_DIR, "../config.json"), 'r') as f:
        data = json.load(f)
    return data['Communication']['port']
