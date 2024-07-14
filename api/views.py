from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd

class GenerateRegexAPI(APIView):
    def post(self, request):
        try:
            data_json = self.process_csv()
            return Response({"message": "Data processed successfully", "data": data_json}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"error": "No 'Email' column found."}, status=status.HTTP_400_BAD_REQUEST)
        except FileNotFoundError:
            return Response({"error": "CSV file not found."}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def read_file(self, path):
        # Reads a CSV or Excel file into a DataFrame based on the file extension.
        if path.endswith('.csv'):
            return pd.read_csv(path)
        elif path.endswith('.xls') or path.endswith('.xlsx'):
            return pd.read_excel(path, header=1)
        else:
            raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")

    def apply_regex(self, dataframe, column_name, regex_pattern, replacement='REDACTED'):
        # Applies regex replacement to specified column in the DataFrame.
        if column_name in dataframe.columns:
            dataframe[column_name] = dataframe[column_name].astype(str).replace(regex_pattern, replacement, regex=True)
        else:
            raise KeyError(f"Column {column_name} not found in DataFrame.")

    def process_csv(self):
        # Processes the CSV or excel file to apply regex and convert to JSON.
        csv_file_path = 'test.csv'
        df = self.read_file(csv_file_path)
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'
        self.apply_regex(df, 'Email', email_regex)
        return df.to_json(orient='records')
