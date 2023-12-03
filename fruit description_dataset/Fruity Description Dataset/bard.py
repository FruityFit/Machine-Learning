
# Replace "YOUR_API_KEY" with the actual API Key obtained earlier

import requests
import json

# Replace "YOUR_API_KEY" with the actual API Key obtained in Step 1
API_KEY = "AIzaSyAKcyiQBnuQNxp5kkBTZCmm5E5p61uCjRE"
URL = "https://bard.googleapis.com/v1/generate"
def get_bard_response(query):
	response = requests.post(URL, headers=
				{"Authorization": "Bearer " + API_KEY},
							json={"query": query})
	print(response)
	data = json.loads(response.content)
	return data["text"]
def main():
	query = "Geeksforgeeks"
	response = get_bard_response(query)
	print("Google Bard Response:")
	print(response)

if __name__ == "__main__":
	main()


if __name__ == "__main__":
	main()
