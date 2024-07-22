import json
import base64
import firebase_admin
from firebase_admin import credentials

with open('./firebase-adminsdk.json', 'r') as file:
    firebase_config = json.load(file)

project_id = firebase_config['project_id']

import os

if not firebase_admin._apps:
    # Get the Base64 encoded string from environment variable
    encoded_creds = os.getenv('GOOGLE_CONFIG_BASE64')
    if encoded_creds is None:
        raise ValueError("GOOGLE_CONFIG_BASE64 environment variable is not set")

    # Decode the Base64 string
    decoded_bytes = base64.b64decode(encoded_creds)
    
    # Convert bytes to ASCII string then parse JSON
    service_account_info = json.loads(decoded_bytes.decode('ascii'))
    
    # Create a credential object from the service account info
    cred = credentials.Certificate(service_account_info)
    
    # Initialize the Firebase Admin SDK
    firebase_admin.initialize_app(cred, {
      'storageBucket': f'{project_id}.appspot.com'
  })

