import datetime
import json
import os
import tempfile
from firebase_admin import storage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rhombus_project.services import RegexService
from rhombus_project.utils import DataProcessor, FileHandler

class GenerateRegexAPI(APIView):
    def post(self, request):
        description = request.data.get('description')
        file_url = request.data.get('file_url')

        if not description:
            return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)

        if not file_url:
            return Response({"error": "File URL is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        column_name = None

        try:
            regex_info = json.loads(RegexService.generate_regex(description))
            print(regex_info)
            column_name = regex_info['column_name']
            regex_pattern = regex_info['regex_pattern']
            replacement_term = regex_info['replacement_term']

            # Download the file from Firebase Storage
            bucket = storage.bucket()
            blob = bucket.blob(file_url)
            _, temp_file_path = tempfile.mkstemp(suffix=os.path.splitext(file_url)[1])
            blob.download_to_filename(temp_file_path)

            # Read the CSV file using FileHandler
            df = FileHandler.read_file(temp_file_path)
            DataProcessor.apply_regex(df, column_name, regex_pattern, replacement_term)

            # Save the processed DataFrame to a new temporary file
            _, processed_file_path = tempfile.mkstemp(suffix=os.path.splitext(file_url)[1])
            df.to_csv(processed_file_path, index=False) 

            # Upload the processed file to Firebase Storage
            processed_blob = bucket.blob(f'processed/{os.path.basename(file_url)}')
            processed_blob.upload_from_filename(processed_file_path)

            # Generate download URL for the uploaded file
            download_url = processed_blob.generate_signed_url(version='v4', expiration=datetime.timedelta(minutes=15), method='GET')

            data_json = df.to_json(orient='records')
            
            return Response({"message": "Data processed successfully", "data": data_json, "new_url": download_url}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"error": f"{column_name} column not found."}, status=status.HTTP_400_BAD_REQUEST)
        except FileNotFoundError:
            return Response({"error": "CSV file not found."}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)