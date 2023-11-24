import csv
import re
from collections import Counter

# Define a function to extract unique names from a URL
def extract_unique_names(url):
    pattern = r'http://timesofindia.indiatimes.com//(.*?)/'
    #pattern = r'https://www.ndtv.com/(.*?)/'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

# Input and output CSV file paths
input_csv_file = '../raw_data/TOI_2018_data.csv'
target_words = ['elections','city','india','politics','business']
# Read the input CSV file and filter rows with matching names
matching_rows = []

with open(input_csv_file, 'r', newline='') as input_csv:
    reader = csv.DictReader(input_csv)
    fieldnames = reader.fieldnames

    for row in reader:
        url = row['URL']
        unique_name = extract_unique_names(url)
        if unique_name and any(word in unique_name for word in target_words):
            matching_rows.append(row)

# Update the existing CSV file with the matching rows
with open(input_csv_file, 'w', newline='') as output_csv:
    writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(matching_rows)

print(f"Rows containing the words {target_words} updated in {input_csv_file}")
