from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser(description='Join Gmeet automatically with given credentials.')
	parser.add_argument('-e', dest='email', required=True,
						help='Email used to get into google')
	parser.add_argument('-p', dest='password', required=True,
						help='Password of your google account')
	parser.add_argument('-m', dest='meet', required=True,
						help='Gmeet link to join')
	parser.add_argument('-d', dest='desc', help='Description of the meet')
	return parser.parse_args()

def login(mail_address, password):
	time.sleep(1)

	WebDriverWait(driver, 10).until(EC.url_contains(("accounts.google.com/signin/")))

	# Types in Email Id
	driver.find_element_by_id("identifierId").send_keys(mail_address)
	driver.find_element_by_id("identifierNext").click()

	time.sleep(2)

	# Types in Password
	driver.find_element_by_xpath(
		'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
	driver.find_element_by_id("passwordNext").click()

def turn_off_mic_cam():
	time.sleep(1)

	WebDriverWait(driver, 10).until(EC.url_contains(("meet.google.com")))

	# Turns off Microphone
	driver.find_element_by_xpath(
		"//div[@class='IYwVEf HotEze uB7U9e nAZzG']").click()
	
	time.sleep(1)
	
	# Turns off Camera
	driver.find_element_by_xpath(
		"//div[@class='IYwVEf HotEze nAZzG']").click()

def join():
	time.sleep(5)
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt")))

	# Joins Google Meet
	driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

def exit():
	time.sleep(600)
	while int(driver.find_element_by_xpath("//div[@class='uGOf1d']").text) > 30:
		print(time.strftime("%X"))
	
	driver.close()

# Main
print('\nSession started!\n')

args = parse_arguments()

print(f'Meet Id: {args.meet}')
print(f'Description: {args.desc}')

opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("excludeSwitches", [
	"disable-popup-blocking"
])
opt.add_experimental_option("prefs", {
	"profile.default_content_setting_values.media_stream_mic": 1,
	"profile.default_content_setting_values.media_stream_camera": 1,
	"profile.default_content_setting_values.geolocation": 0,
	"profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(options=opt, executable_path='web_drivers/chromedriver.exe')
driver.implicitly_wait(5)

retry = 0
while driver.current_url.find('accounts.google.com/signin/') == -1 and retry < 10:
	retry += 1
	driver.get(args.meet)
	time.sleep(2)

login(args.email, args.password)

turn_off_mic_cam()

# join()

# exit()

print('\nSession ended!')