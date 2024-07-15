import pandas as pd

class FileHandler:
    # Reads a CSV or Excel file into a DataFrame based on the file extension.    
    def read_file(path):
        if path.endswith('.csv'):
            return pd.read_csv(path)
        elif path.endswith('.xls') or path.endswith('.xlsx'):
            return pd.read_excel(path, header=1)
        else:
            raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")

class DataProcessor:
    # Apply regex replacement to specified column in the DataFrame.
    def apply_regex(dataframe, column_name, regex_pattern, replacement_term):
        if column_name in dataframe.columns:
            dataframe[column_name] = dataframe[column_name].astype(str).replace(regex_pattern, replacement_term, regex=True)
        else:
            raise KeyError(f"Column {column_name} not found in DataFrame.")
