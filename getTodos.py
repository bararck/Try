import requests

# Define the endpoint and parameters
endpoint = "https://gorest.co.in/public/v2/users/7074321/todos"
params = {
    "per_page": 10  # Set the number of items per page to 10
}

# Perform the GET request
response = requests.get(endpoint, params=params)

# Check if the request was successful
if response.status_code == 200:
    todos = response.json()
    
    # Validate the number of items returned
    if len(todos) == 10:
        print("Test Passed: The response contains exactly 10 items.")
    else:
        print(f"Test Failed: The response contains {len(todos)} items instead of 10.")
else:
    print(f"Failed to retrieve todos. Status code: {response.status_code}")

# Optionally, print the todos for verification
for todo in todos:
    print(todo)
