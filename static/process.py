import requests


def render(data):
    print("Processing ...")
    r = requests.get("https://google.ca")
    for k,v in data.items():
        print(f"{k}: {v}")
