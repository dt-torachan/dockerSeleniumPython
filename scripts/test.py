from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get("https://henderscheme:uchenderscheme@test-henderscheme.bb-f.net")
page_width = driver.execute_script('return document.body.scrollWidth')
page_height = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(page_width, page_height)
driver.save_screenshot('/dev/shm/screenshot.png')
driver.quit()
exit()