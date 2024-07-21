import json
import firebase_admin
from firebase_admin import credentials

with open('./firebase-adminsdk.json', 'r') as file:
    firebase_config = json.load(file)

project_id = firebase_config['project_id']

cred = credentials.Certificate(firebase_config)
firebase_admin.initialize_app(cred, {
    'storageBucket': f'{project_id}.appspot.com'
})

