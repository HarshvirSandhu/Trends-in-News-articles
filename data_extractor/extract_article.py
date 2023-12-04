from requests import Session
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import re
count = 0


def fetch_article_content(url, session):
    global count
    try:
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        article_content = soup.find('div', {'class': 'sp-cn ins_storybody'})  # Modify this based on the structure of the webpage
        return article_content.get_text() if article_content else None
    except Exception as e:
        print(f"Error fetching article content: {str(e)}")
        count+=1
        return None

def NDTV_data_extractor(url, session):
    global count
    try:
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        article_content = soup.find('div', {'class': 'sp-cn ins_storybody'})  # Modify this based on the structure of the webpage
        date_content = soup.find('span', {'class': 'pst-by_lnk'})
        
        # if date_content:
        #     date_pattern = r'Updated: (\w+ \d+, \d+)\d+:?\d+ (AM|PM) IST'
        #     match = re.search(date_pattern, date_content.get_text())
        #     if match:
        #         date_str = match.group(1)
        #     else:
        #         date_str = None

        return article_content.get_text(),date_content.get_text() if article_content and date_content else None
    except Exception as e:
        print(f"Error fetching article content: {str(e)}")
        count+=1
        return None,None

path = '../raw_data/NDTV_2017_data.csv'
#path = '../raw_data/test.csv'
df = pd.read_csv(path)
# del df['Unnamed: 0']
print(df['URL'].shape)
content = []
day = []
session = Session()
pbar = tqdm(df['URL'].tolist(), desc="Processing URLs")
for idx, link in enumerate(pbar):
    content.append(NDTV_data_extractor(url=link, session=session)[0])
    day.append(NDTV_data_extractor(url=link, session=session)[1])
    pbar.set_postfix({'Number of failed URLs': count})

df['article'] = content
df['day_count'] = day
df.to_csv(path)
