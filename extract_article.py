import requests
from bs4 import  BeautifulSoup

def fetch_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        article_content = soup.find('div', {'class': '_s30J clearfix'})  # Modify this based on the structure of the webpage
        return article_content.get_text() if article_content else None
    except Exception as e:
        print(f"Error fetching article content: {e}")
        return None

print(fetch_article_content('http://timesofindia.indiatimes.com//city/jaipur/voluntary-load-disclosure-scheme-from-today-discom/articleshow/50402761.cms'))