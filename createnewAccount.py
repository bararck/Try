import requests
import json

# Endpoint and API token
url = "https://gorest.co.in/public/v2/users"
api_token = "a468f13271042789f7cb3b9c0920fc0dc8835a924d377887e701ffa1d61c5ee1"

# User data to be posted
user_data = {
    "name": "Test",
    "email": "john.test@example.com",
    "gender": "male",
    "status": "active"
}

# Headers for the request
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(user_data))

# Check the response
if response.status_code == 201:
    print("User created successfully.")
    print("Response:", response.json())
else:
    print("Failed to create user.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)