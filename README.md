Python 3.10.9
django-admin --version 5.0.7

Step 1: Create Environment Variables
Create a .env file in the main project folder.
Add the following line to the file, replacing your-openai-apikey with your actual OpenAI API key:
OPENAI_APIKEY=your-openai-apikey

Step 2: Set Up Firebase
1. Create a New Firebase Project:
  - Go to the Firebase Console.
  - Click on "Add project" and follow the instructions to create a new Firebase project.
2. Download Firebase Admin SDK JSON File:
  - In your Firebase project, navigate to Project settings > Service accounts.
  - Click "Generate new private key" and download the JSON file.
3. Configure Your Project:
  - Move the downloaded JSON file to the main project folder.
  - Rename the file to firebase-adminsdk.json.

Step 3: Build the Project
1. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
2. Install Dependencies:
pip install -r requirements.txt

Step 4: Run the Project
1. Migrate the Database:
python manage.py migrate
2. Start the Server:
python manage.py runserver





