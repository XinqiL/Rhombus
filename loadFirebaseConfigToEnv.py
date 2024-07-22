import json
import base64

# Define the path to the JSON file and the output .env file
json_file_path = './firebase-adminsdk.json'
env_file_path = '.env'

# Read the JSON file
with open(json_file_path, 'r') as file:
    # Load JSON content
    service_account_info = json.load(file)

# Convert the dictionary to a JSON string
json_str = json.dumps(service_account_info)

# Encode this JSON string to Base64
encoded_base64 = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

# Append or create the .env file and write the Base64 string
with open(env_file_path, 'a+') as file:
    # Move the cursor to the beginning of the file
    file.seek(0)
    # Read the content to check if it's empty or already contains data
    content = file.read()
    # If not empty and does not end with a newline, add one
    if content and not content.endswith('\n'):
        file.write('\n')
    file.write(f"GOOGLE_CONFIG_BASE64={encoded_base64}\n")

print("Base64 encoded string has been appended to or written in the .env file.")
