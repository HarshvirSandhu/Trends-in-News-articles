from requests import Session
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
count = 0


def fetch_article_content(url, session):
    global count
    try:
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        article_content = soup.find('div', {'class': '_s30J clearfix'})  # Modify this based on the structure of the webpage
        return article_content.get_text() if article_content else None
    except Exception as e:
        print(f"Error fetching article content: {str(e)}")
        count+=1
        return None

path = '../raw_data/TOI_2015_data.csv'
df = pd.read_csv(path)
del df['Unnamed: 0']
print(df['URL'].shape)
content = []
session = Session()
pbar = tqdm(df['URL'].tolist(), desc="Processing URLs")
for idx, link in enumerate(pbar):
    content.append(fetch_article_content(url=link, session=session))
    pbar.set_postfix({'Number of failed URLs': count})

df['article'] = content
df.to_csv(path)
