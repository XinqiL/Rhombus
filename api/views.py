import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rhombus_project.services import RegexService
from rhombus_project.utils import DataProcessor, FileHandler

class GenerateRegexAPI(APIView):
    def post(self, request):
        description = request.data.get('description')
        if not description:
            return Response({"error": "Description is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            regex_info = json.loads(RegexService.generate_regex(description))
            print(regex_info)
            column_name = regex_info['column name']
            regex_pattern = regex_info['regex pattern']
            replacement_term = regex_info['replacement term']

            csv_file_path = 'test.csv'  # To be modified after frontend implementation
            df = FileHandler.read_file(csv_file_path)
            DataProcessor.apply_regex(df, column_name, regex_pattern, replacement_term)
            data_json = df.to_json(orient='records')
            
            return Response({"message": "Data processed successfully", "data": data_json}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"error": f"{column_name} column not found."}, status=status.HTTP_400_BAD_REQUEST)
        except FileNotFoundError:
            return Response({"error": "CSV file not found."}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)