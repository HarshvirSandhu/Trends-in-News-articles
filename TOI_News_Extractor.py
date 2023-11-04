import csv
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define a function to extract unique names from a URL
def extract_unique_names(url):
    pattern = r'http://timesofindia.indiatimes.com//(.*?)/'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    else:
        return None

# Define a function to fetch and extract article content from a URL
def fetch_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        article_content = soup.find('div', {'class': 'article_content'})  # Modify this based on the structure of the webpage
        return article_content.get_text() if article_content else None
    except Exception as e:
        print(f"Error fetching article content: {e}")
        return None

# Input CSV file path
input_csv_file = 'TOI_2015_data_train.csv'  # Replace with your input CSV file path

# Read the existing CSV file into a DataFrame
df = pd.read_csv(input_csv_file)

# Add a new column 'article data' and fetch article data for each row
df['article data'] = df['URL'].apply(lambda x: fetch_article_content(x))

# Save the modified DataFrame back to the same CSV file
df.to_csv(input_csv_file, index=False)

print(f"'article data' column added and data saved to {input_csv_file}")
