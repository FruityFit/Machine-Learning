import requests
url = "http://127.0.0.1:5000/chat"
headers = {"Content-Type": "application/json"}
data = {"user_input": "Hi"}


response = requests.post(url, json=data, headers=headers)
response.raise_for_status()  # Raises an HTTPError for bad responses
