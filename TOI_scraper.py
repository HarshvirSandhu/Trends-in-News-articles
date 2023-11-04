from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

mm_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
mappings = dict()
skipped = 0
count = 0
mm=0
while count <= 365 and mm<len(mm_list):
    try:
        browser = webdriver.Chrome()
        browser.get(f'https://timesofindia.indiatimes.com/2015/1/1/archivelist/year-2015,month-{mm_list[mm]},starttime-{42005+count}.cms')
        # time.sleep(1)
        links = browser.find_elements(By.XPATH,
                                       '//*[@style="font-family:arial ;font-size:12;font-weight:bold; color: #006699"]')
        # print(links, links[1].text)
        print('-------- NEW DATE ----------')
        in_html = [j.find_elements(By.TAG_NAME, 'a') for j in links][1]
        print(len(in_html), '{{{{{{{{{{{')
        for title in in_html:
            mappings[title.text] = title.get_attribute('href')
        browser.quit()
        count += 1
    except:
        mm+=1

df = pd.DataFrame({'Title': list(mappings.keys())})
df['URL'] = list(mappings.values())
# df['Month'] = months
df.to_csv('TOI_2015_data.csv')
print(skipped)
