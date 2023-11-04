import csv
import re

# Define a function to extract unique names from a URL
def extract_unique_names(url):
    # Use a regular expression to find names after "http://timesofindia.indiatimes.com//"
    pattern = r'http://timesofindia.indiatimes.com//(.*?)/'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

# Input and output CSV file paths
input_csv_file = 'TOI_2015_data.csv' 
output_csv_file = 'TOI_2015_data_train.csv'  
target_words = ['budget-2015','india','city','spirituality','business','world','sports',]  

# Read the input CSV file and filter rows with matching names
matching_rows = []

with open(input_csv_file, 'r', newline='') as input_csv:
    reader = csv.DictReader(input_csv)
    for row in reader:
        url = row['URL']
        unique_name = extract_unique_names(url)
        if unique_name and any(word in unique_name for word in target_words):
            matching_rows.append(row)

# Write the matching rows to an output CSV file
with open(output_csv_file, 'w', newline='') as output_csv:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(matching_rows)

print(f"Rows containing the words {target_words} saved to {output_csv_file}")
