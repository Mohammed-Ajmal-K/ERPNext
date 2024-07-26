import requests
import uuid  # For generating unique IDs

base_url = 'http://localhost:8000/api/resource/Lead'
auth = ('1fabee6cc5d4bf1', '8e7f675a48d130b')

def create_lead():
    unique_email = f"messi.hoi.{uuid.uuid4().hex[:6]}@example.com"
    data_create = {
        "first_name": "lional",
        "last_name": "Messi",
        "email_id": unique_email,
        "mobile_no": "+985665698",
        "company": "TechNext",
        "country": "India"
    }
    response_create = requests.post(base_url, json=data_create, auth=auth)
    if response_create.status_code in [200, 201]:
        print("Create Lead:", response_create.json())
        lead_name = response_create.json().get('data', {}).get('name')
        save_lead_name(lead_name)  # Save lead_name to a file
        return lead_name
    else:
        print("Failed to create lead:", response_create.status_code, response_create.text)
        return None

def read_lead():
    lead_name = load_lead_name()
    if lead_name:
        response_read = requests.get(f"{base_url}/{lead_name}", auth=auth)
        if response_read.status_code == 200:
            print(f"Read Lead '{lead_name}':", response_read.json())
        else:
            print(f"Failed to read lead '{lead_name}':", response_read.status_code, response_read.text)
    else:
        print("No lead created yet. Create a lead first.")

def update_lead():
    lead_name = load_lead_name()
    if lead_name:
        data_update = {
            "mobile_no": "+1987654321"
        }
        response_update = requests.put(f"{base_url}/{lead_name}", json=data_update, auth=auth)
        if response_update.status_code == 200:
            print(f"Update Lead '{lead_name}':", response_update.json())
        else:
            print(f"Failed to update lead '{lead_name}':", response_update.status_code, response_update.text)
    else:
        print("No lead created yet. Create a lead first.")

# def delete_lead():
#     lead_name = load_lead_name()
#     if lead_name:
#         response_delete = requests.delete(f"{base_url}/{lead_name}", auth=auth)
#         if response_delete.status_code in [202, 204]:
#             print(f"Delete Lead '{lead_name}': Success")
#             clear_lead_name()  # Clear lead_name after deletion
#         else:
#             print(f"Failed to delete lead '{lead_name}':", response_delete.status_code, response_delete.text)
#     else:
#         print("No lead created yet. Create a lead first.")

def save_lead_name(lead_name):
    with open("lead_name.txt", "w") as file:
        file.write(lead_name)

def load_lead_name():
    try:
        with open("lead_name.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def clear_lead_name():
    try:
        with open("lead_name.txt", "w") as file:
            file.write("")
    except FileNotFoundError:
        pass

# Main function to orchestrate the operations
def main():
    # Uncomment and execute each operation one at a time
    lead_name = create_lead()
    if lead_name:
        read_lead()
        update_lead()
        # delete_lead()

if __name__ == "__main__":
    main()
