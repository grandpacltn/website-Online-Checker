import requests

url = input("Enter website URL: ")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Website is online!")
    else:
        print("Website is down!")
except:
    print("Invalid URL or no internet connection.")