import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.add_argument('--profile-directory=Default')
options.add_argument('--user-data-dir=//Users//harshuljain//Library//Application Support//Google//Chrome//Default')
driver = uc.Chrome(executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", options=options)

driver.get('https://www.byerstoyota.com/')
time.sleep(50)