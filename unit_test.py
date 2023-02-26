import requests
URL = "https://atg.world"
try:
    response = requests.head(URL)
except Exception as e:
    print(f"Not OK: {str(e)}")
else:
    if response.status_code == 200:
        print("OK")
    else:
        print(f"NOT OK: HTTP response code {response.status_code}")
