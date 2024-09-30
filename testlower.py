import requests

# Define the base URL of your FastAPI application
base_url = "http://127.0.0.1:8502"  # Update with your actual server address

# Define the input data as a dictionary
data = {
    "input2": "HELLO"
}

# Send a POST request to the /sum endpoint
response = requests.post(f"{base_url}/lower", json=data)

# Check the response status code
if response.status_code == 200:
    # If the response is successful, print the result
    result = response.json()
    print("lower:", result["lower"])
else:
    # If the response is not successful, print an error message
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.text)
