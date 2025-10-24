import json
import requests

URL = "http://localhost:8000/predict"

sample = {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}

def run():
    r = requests.post(URL, json=sample)
    try:
        r.raise_for_status()
    except Exception as e:
        print("Request failed:", r.status_code, r.text)
        return
    print("Response:", json.dumps(r.json(), indent=2))

if __name__ == "__main__":
    run()