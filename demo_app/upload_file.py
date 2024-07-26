import requests
from requests.auth import HTTPBasicAuth

# Your ERPNext/Frappe instance URL
base_url = "http://192.168.1.49:8000/"

# Your API key and secret
api_key = "1fabee6cc5d4bf1"
api_secret = "8e7f675a48d130b"

# File to upload
file_path = "/home/ajmal/Downloads/download.jpeg"

# API endpoint to upload file
upload_url = f"{base_url}/api/method/upload_file"

# Read the file content
with open(file_path, 'rb') as file:
    # Prepare the request
    files = {
        'file': file,
        'is_private': (None, '1'),  # Set to '0' if the file should be public
    }
    
    # Send the request with SSL verification disabled (for testing purposes)
    try:
        response = requests.post(upload_url, files=files, auth=HTTPBasicAuth(api_key, api_secret), verify=False)
        
        # Check the response
        if response.status_code == 200:
            print("File uploaded successfully")
            print("Response:", response.json())
        else:
            print("Failed to upload file")
            print("Response:", response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

