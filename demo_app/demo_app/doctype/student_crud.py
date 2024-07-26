#  import requests

# base_url = 'http://localhost:8000/api/resource/Student'
# auth = ('1fabee6cc5d4bf1', '8e7f675a48d130b')

# name1 = "Messi"

# # Check if the student already exists
# response = requests.get(f"{base_url}/{name1}", auth=auth)
# if response.status_code == 200:
#     print("Student already exists:", response.json())
# else:
#     # Create
#     data = {
#         "name1": name1,
#         "register_number": 75,
#         "dob": "2000-01-01",
#         "gender": "Male"
#     }
#     response = requests.post(base_url, json=data, auth=auth)
#     print("Create:", response.json())

# # Read
# response = requests.get(f"{base_url}/{name1}", auth=auth)
# print("Read:", response.json())

# # Update
# data = {
#     "dob": "2000-01-02"
# }
# response = requests.put(f"{base_url}/{name1}", json=data, auth=auth)
# print("Update:", response.json())

# # Delete
# response = requests.delete(f"{base_url}/{name1}", auth=auth)
# print("Delete:", response.status_code)  # 204 indicates success


import requests

base_url = 'http://localhost:8000/api/resource/Student'
auth = ('1fabee6cc5d4bf1', '8e7f675a48d130b')

name1 = "Messi"

# Check if the student already exists
response = requests.get(f"{base_url}/{name1}", auth=auth)
if response.status_code == 200:
    print("Student already exists:", response.json())
else:
    # Create
    data = {
        "name1": name1,  # Corrected key from "name1" to "name"
        "register_number": 75,
        "dob": "2000-01-01",
        "gender": "Male"
    }
    response = requests.post(base_url, json=data, auth=auth)
    if response.status_code in [200, 201]:  # Check for successful creation
        print("Create:", response.json())
    else:
        print("Failed to create student:", response.status_code, response.text)

# Read
response = requests.get(f"{base_url}/{name1}", auth=auth)
if response.status_code == 200:
    print("Read:", response.json())
else:
    print("Failed to read student:", response.status_code, response.text)

# Update
data = {
    "dob": "2000-01-02"
}
response = requests.put(f"{base_url}/{name1}", json=data, auth=auth)
if response.status_code == 200:
    print("Update:", response.json())
else:
    print("Failed to update student:", response.status_code, response.text)

# Delete
# response = requests.delete(f"{base_url}/{name1}", auth=auth)
# if response.status_code in [202, 204]:
#     print("Delete: Success")
# else:
#     print("Failed to delete student:", response.status_code, response.text)

