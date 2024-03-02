import requests

# Base URL of your Google Apps Script web app
base_url = "YOUR_SCRIPT_WEB_APP_URL"

# Function to send GET request
def get_records():
    url = base_url + "?action=getRecords"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return "Error: Unable to fetch records"

# Function to send POST request
def create_record(title, author, isbn):
    url = base_url + f"?action=createRecord&title={title}&author={author}&isbn={isbn}"
    response = requests.post(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to create record"

# Function to send PUT request
def update_record(row, title, author, isbn):
    url = base_url + f"?action=updateRecord&row={row}&title={title}&author={author}&isbn={isbn}"
    response = requests.put(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to update record"

# Function to send DELETE request
def delete_record(row):
    url = base_url + f"?action=deleteRecord&row={row}"
    response = requests.delete(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error: Unable to delete record"

# Example usage
# Replace the base_url with your deployed web app URL
base_url = "YOUR_SCRIPT_WEB_APP_URL"

# Get records
print(get_records())

# Create record
print(create_record("New Book", "New Author", "1234567890"))

# Update record
print(update_record(2, "Updated Book", "Updated Author", "0987654321"))

# Delete record
print(delete_record(2))
