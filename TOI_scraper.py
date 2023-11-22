from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

mm_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
mappings = dict()
year = 2021
skipped = 0
count = 0
mm = 0
day_map = dict()
browser = webdriver.Chrome()
while count <= 365 and mm < len(mm_list):
    try:
        browser.get(f'https://timesofindia.indiatimes.com/{year}/1/1/archivelist/year-{year},month-{mm_list[mm]},starttime-{44197+count}.cms')
        # time.sleep(1)
        links = browser.find_elements(By.XPATH,
                                       '//*[@style="font-family:arial ;font-size:12;font-weight:bold; color: #006699"]')
        # print(links, links[1].text)
        print('-------- NEW DATE ----------')
        in_html = [j.find_elements(By.TAG_NAME, 'a') for j in links][1]
        print(len(in_html), '{{{{{{{{{{{')
        for title in in_html:
            mappings[title.text] = title.get_attribute('href')
            day_map[title.text] = count
        count += 1
    except:
        mm+=1

browser.quit()
df = pd.DataFrame({'Title': list(mappings.keys())})
df['URL'] = list(mappings.values())
print(df.shape, len(list(day_map.values())))
df['Day'] = list(day_map.values())
df.to_csv(f'TOI_{year}_data.csv')
print(skipped)
