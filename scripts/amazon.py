from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('-disable-dev-shm-usage')  
driver = webdriver.Chrome(options=options)

driver.get("https://www.amazon.co.jp/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
email_box = driver.find_element_by_id('ap_email')
email_box.send_keys("xxxxxxx@abc.com")
continue_btn = driver.find_element_by_id('continue')
continue_btn.click()
email_box = driver.find_element_by_id('ap_password')
email_box.send_keys("xxxxxxxx")
signin_btn = driver.find_element_by_id('signInSubmit')
signin_btn.click()

page_width = driver.execute_script('return document.body.scrollWidth')
page_height = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(page_width, page_height)
driver.save_screenshot('/dev/shm/ss/screenshot_amazon.png')
driver.quit()
exit()