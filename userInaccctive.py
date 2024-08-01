import requests

# Define the endpoint for retrieving users by ID
base_url = "https://gorest.co.in/public/v2/users"

def get_user_by_id(user_id):
    # Build the full URL with the user ID
    url = f"{base_url}/{user_id}"
    
    print(f"Requesting URL: {url}")  # Debugging line to show the full URL
    
    # Perform the GET request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        user_data = response.json()
        
        # Validate that the user has the status 'inactive'
        if user_data.get('status') == 'inactive':
            print("Test Passed: User has the status 'inactive'.")
            print("User Data:")
            print(user_data)
        else:
            print(f"Test Failed: User status is '{user_data.get('status')}' instead of 'inactive'.")
    elif response.status_code == 404:
        print("Error 404: Resource not found. The user ID might be incorrect or the endpoint may be wrong.")
    else:
        print(f"Failed to retrieve user. Status code: {response.status_code}")

# Replace with the actual user ID you want to test
user_id = 7074204

# Call the function to test
get_user_by_id(user_id)
