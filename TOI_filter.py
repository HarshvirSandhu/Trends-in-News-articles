import csv
import re
from collections import Counter

# Define a function to extract unique names from a URL
def extract_unique_names(url):
    pattern = r'http://timesofindia.indiatimes.com//(.*?)/'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

input_csv_file = 'TOI_2015_data.csv'  
output_csv_file = 'Unique_names_in_news.csv'  

# List to store all extracted names
all_names = []

# Read the input CSV file and extract names
with open(input_csv_file, 'r', newline='') as input_csv:
    reader = csv.DictReader(input_csv)
    for row in reader:
        url = row['URL']
        unique_name = extract_unique_names(url)
        if unique_name:
            all_names.append(unique_name)

# Count the occurrences of each unique name
name_counts = Counter(all_names)

# Write the unique names and their counts to an output CSV file
with open(output_csv_file, 'w', newline='') as output_csv:
    writer = csv.writer(output_csv)
    writer.writerow(['Unique Names', 'Count'])
    for name, count in name_counts.items():
        writer.writerow([name, count])

print("Unique names extracted and their counts saved to", output_csv_file)
