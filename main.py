from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome()
driver.implicitly_wait(10)

zavodpt_link = 'https://zavod-pt.ru/'

list = []

with open('list.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        list.append(' '.join(row))

print(list)
def link_crawling():
    driver.get(url=zavodpt_link)
    driver.maximize_window()

    link_crawling_list = []
    for article in list:
        try:
            link_crawling_list_row = []

            find_field = driver.find_element(By.ID, 'title-search-input_fixed')
            find_field.click()
            find_field.send_keys(article)
            find_field.send_keys(Keys.ENTER)
            h1_text = driver.find_element(By.ID, 'pagetitle').text

            link_crawling_list_row.append(h1_text)
            link_crawling_list_row.append(article)
            link_crawling_list_row.append(driver.current_url)
            link_crawling_list.append(link_crawling_list_row)

            print(f'Status №{list.index(article)} is ok from {len(list)}')
            print(link_crawling_list_row)

            driver.get(url=zavodpt_link)

        except Exception as ex:
                link_crawling_list.append(link_crawling_list_row)
                print(ex)
                driver.get(url=zavodpt_link)
                continue

    with open('test.csv', 'w') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        for item in link_crawling_list:
            writer.writerow(item)
    return


try:
    link_crawling()

except Exception as ex:
    print(ex)
    pass

finally:
    print('Done')
    driver.close()
    driver.quit()
