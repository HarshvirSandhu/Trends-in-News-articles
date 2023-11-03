from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
dd = 11
mm_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
year=2015
mappings = dict()
months = []
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
        # count-=1


# for mm in mm_list:
#     browser = webdriver.Chrome()
#     browser.get(f'https://timesofindia.indiatimes.com/archive/year-2015,month-{mm}.cms')
#     time.sleep(1)
#     # try:
#     calender = browser.find_element(By.ID, 'calender')
#     dates = calender.find_elements(By.TAG_NAME, 'td')
#     date_indices = [i for i, item in enumerate(dates) if item.text.isnumeric()]
#     for d in date_indices:
#         print(dates[d].get_attribute('innerHTML'), '\n\n\n')
#     print(len(date_indices))
#     print(calender.text)
#     for i in date_indices:
#     # try:
#         print(i, len(date_indices))
#         print(browser.current_url)
#         dates[i].find_element(By.TAG_NAME, 'a').click()
#         time.sleep(3)
#         print(browser.current_url)
#
#         links = browser.find_elements(By.XPATH,
#                                       '//*[@style="font-family:arial ;font-size:12;font-weight:bold; color: #006699"]')
#         # print(links, links[1].text)
#         print('-------- NEW DATE ----------')
#         in_html = [j.find_elements(By.TAG_NAME, 'a') for j in links][1]
#         print(len(in_html), '{{{{{{{{{{{')
#         for title in in_html:
#             mappings[title.text] = title.get_attribute('href')
#         # months.append(mm)
#         browser.quit()
#         browser = webdriver.Chrome()
#         browser.get(f'https://timesofindia.indiatimes.com/archive/year-2015,month-{mm}.cms')
#         time.sleep(5)
#             # except Exception as e:
#             #     print('Skipping a date', browser.current_url)
#             #     print(e)
#             #     skipped+=1
#             #     browser.get(f'https://timesofindia.indiatimes.com/archive/year-2015,month-{mm}.cms')
#             #     time.sleep(2)
#     # except Exception as e:
#     #     print(e)
#     print('################ NEW MONTH #######################')
#     browser.back()
#     time.sleep(2)
#         # print(mappings)
#     browser.quit()

df = pd.DataFrame({'Title': list(mappings.keys())})
df['URL'] = list(mappings.values())
# df['Month'] = months
df.to_csv('TOI_2015_data.csv')
print(skipped)