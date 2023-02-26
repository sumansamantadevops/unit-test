import requests
URL = "https://atg.world"
try:
    response = requests.head(URL)
except Exception as e:
    print(f"Fail: {str(e)}")
else:
    if response.status_code == 200:
        print("Pass")
    else:
        print(f"NOT OK: HTTP response code {response.status_code}")
