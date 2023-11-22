import pandas as pd
import requests
from bs4 import BeautifulSoup

mm_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
year = 2021
mappings = dict()
for m in mm_list:
    url = f'https://archives.ndtv.com/articles/{year}-{m}.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all(class_="ins_lftcont640")

    for link in links:
        articles = link.find_all('li')
        for one in articles:
            mappings[one.text.strip('\n')] = str(one.find('a', href=True)).split('\"')[1]

df = pd.DataFrame({'Title': list(mappings.keys())})
df['URL'] = list(mappings.values())
df.to_csv(f'raw_data/NDTV_{year}_data.csv')
print(len(mappings))