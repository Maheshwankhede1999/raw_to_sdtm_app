import os
import pandas as pd
from constants import PathOfFile

def process_dm_files(raw_folder, output_folder):
    # Define prefixes for each file type
    raw_folder_prefixes = {
        'AE': 'ae_'
    }
    output_folder_prefixes = {
        'AE': 'ae'
    }

    # Initialize dictionaries to store schemas
    raw_schemas = {}
    output_schemas = {}

    # Process raw files
    for file_type, prefix in raw_folder_prefixes.items():
        raw_files = [file for file in os.listdir(raw_folder) if file.startswith(prefix)]
        if raw_files:
            raw_schemas[file_type] = {}
            for file in raw_files:
                file_path = os.path.join(raw_folder, file)
                try:
                    df = pd.read_csv(file_path)  # Assuming CSV format
                    raw_schemas[file_type][file] = df.dtypes.to_dict()
                except Exception as e:
                    print(f"Error reading raw file '{file}': {e}")

    # Process output files
    for file_type, prefix in output_folder_prefixes.items():
        output_files = [file for file in os.listdir(output_folder) if file.startswith(prefix)]
        if output_files:
            output_schemas[file_type] = {}
            for file in output_files:
                file_path = os.path.join(output_folder, file)
                try:
                    df = pd.read_csv(file_path)  # Assuming CSV format
                    output_schemas[file_type][file] = df.dtypes.to_dict()
                except Exception as e:
                    print(f"Error reading output file '{file}': {e}")

    return raw_schemas, output_schemas

# Example usage
if __name__ == "__main__":
    raw_folder = PathOfFile.raw_folder.value
    output_folder = PathOfFile.output_folder.value
    raw_schemas, output_schemas = process_dm_files(raw_folder, output_folder)
    print("Schemas for files in raw folder:")
    print(raw_schemas)
    print("Schemas for files in output folder:")
    print(output_schemas)
