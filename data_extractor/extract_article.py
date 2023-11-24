import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Check for 404 error
        if response.status_code == 404:
            print(f"Page not found for {url}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        article_content = soup.find('div', {'class': '_s30J clearfix'})  # Modify this based on the structure of the webpage
        return article_content.get_text() if article_content else None
    except Exception as e:
        print(f"Error fetching article content for {url}: {e}")
        return None

csv_path = '../raw_data/TOI_2015_data.csv' 
df = pd.read_csv(csv_path)

df['article'] = df['URL'].apply(fetch_article_content)

df.to_csv(csv_path, index=False)

print("Data extraction and update completed.")

# import requests
# from bs4 import  BeautifulSoup

# def fetch_article_content(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.text, 'html.parser')
#         article_content = soup.find('div', {'class': '_s30J clearfix'})  # Modify this based on the structure of the webpage
#         return article_content.get_text() if article_content else None
#     except Exception as e:
#         print(f"Error fetching article content: {e}")
#         return None

# print(fetch_article_content('http://timesofindia.indiatimes.com//city/jaipur/voluntary-load-disclosure-scheme-from-today-discom/articleshow/50402761.cms'))