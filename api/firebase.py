import os
import json
import base64
import firebase_admin
from firebase_admin import credentials

if not firebase_admin._apps:
    # Get the Base64 encoded string from environment variable
    encoded_creds = os.getenv('GOOGLE_CONFIG_BASE64')
    if encoded_creds is None:
        raise ValueError("GOOGLE_CONFIG_BASE64 environment variable is not set")

    # Decode the Base64 string
    decoded_bytes = base64.b64decode(encoded_creds)
    
    # Convert bytes to ASCII string then parse JSON
    service_account_info = json.loads(decoded_bytes.decode('ascii'))
    
    project_id = service_account_info['project_id']
    # Create a credential object from the service account info
    cred = credentials.Certificate(service_account_info)
    
    # Initialize the Firebase Admin SDK
    firebase_admin.initialize_app(cred, {
      'storageBucket': f'{project_id}.appspot.com'
  })

