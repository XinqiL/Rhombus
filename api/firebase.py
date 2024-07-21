import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('/Users/Xinqi/Desktop/rhombus-project-firebase-adminsdk-kvn3y-4818fc9b7c.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'rhombus-project.appspot.com'
})

