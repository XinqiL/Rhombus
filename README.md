# Regex Replacement Project - Backend

This README details the steps required to set up and run the Django backend, which is integrated with the OpenAI API. The backend is configured to work in conjunction with the frontend setup previously described and uses Firebase Admin SDK as part of its infrastructure.

## Environment and Dependencies

Python 3.10.9

## Step 1: Set Up Firebase

1. Reuse Existing Firebase Project:

- This backend leverages the same Firebase project established for the frontend. Continue with the configuration using the existing project details. For initial setup instructions or further information, please consult the frontend README at https://github.com/XinqiL/rhombus-frontend

2. Download Firebase Admin SDK JSON File:

- In your Firebase project, navigate to `Project settings > Service accounts`.
- Select Python
- Click "Generate new private key" and download the JSON file.

3. Configure Firebase in Your Project:

- Move the downloaded JSON file to the main project folder.
- Rename the file to `firebase-adminsdk.json`.

## Step 2: Create Environment Variables

1. Run the script to create `.env` file and load the Firebase configuration into your environment variables:
   `python loadFirebaseConfigToEnv.py`

2. Add the following line to the file, replacing your-openai-apikey with your actual OpenAI API key:
   `OPENAI_APIKEY=your-openai-apikey`

## Step 3: Create a Virtual Environment

```
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

## Step 4: Install Dependencies

`pip install -r requirements.txt`

## Step 5: Build and Run the Project

1. Migrate the Database:
   `python manage.py migrate`
2. Start the Server:
   `python manage.py runserver`
