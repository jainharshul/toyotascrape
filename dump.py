from selenium import webdriver

url = "https://www.byerstoyota.com/used-vehicles/"

driver = webdriver.Chrome()

driver.get(url)

html = driver.page_source

with open('webpage.html', 'w', encoding='utf-8') as f:
    f.write(html)

driver.quit()
