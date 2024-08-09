import pandas as pd
import os

# Define the correct path to your output directory
_OUTPUT_PATH = '/Users/rravindra0463/Desktop/ai_proj/venv/new_output'  # Replace with your actual path

# Define paths
csv_file_path = os.path.join(_OUTPUT_PATH, 'New_Results_QTR4.csv')
json_file_path = os.path.join(_OUTPUT_PATH, 'New_Results_QTR4.json')

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to a JSON file
df.to_json(json_file_path, orient='records', lines=True, indent=4)

print(f'CSV file has been converted to JSON and saved as: {json_file_path}')
