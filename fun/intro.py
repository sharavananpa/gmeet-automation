from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


def intro():
    driver.get('https://www.google.com/')

    time.sleep(1)

    driver.find_element_by_xpath(
            '//*[@title="Search"]').send_keys('Hey guys!')

    time.sleep(3)

    driver.get('https://i.imgur.com/VZslpj0.png')

    time.sleep(3)

    driver.get('https://www.google.com/')

    time.sleep(1)

    driver.find_element_by_xpath(
            '//*[@title="Search"]').send_keys("Welcome to great kirikalan magic show!")
        
    time.sleep(5)

    driver.find_element_by_xpath(
            '//*[@title="Search"]').send_keys(Keys.CONTROL, 'z')

    driver.find_element_by_xpath(
            '//*[@title="Search"]').send_keys("Looks like you're running this for the first time!")

    time.sleep(5)

    driver.find_element_by_xpath(
            '//*[@title="Search"]').send_keys(Keys.CONTROL, 'z')

    driver.find_element_by_xpath(
            '//*[@title="Search"]').send_keys("I hope this works for you! Cheers!")
        
    time.sleep(5)

    f = open("hack.txt", "w")
    f.write("Haha! funny fugger. You're hacked!")
    f.close()

# Main
print("HELLLOOOOOO!!!!")
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

driver = webdriver.Chrome(options=opt, executable_path='../web_drivers/chromedriver.exe')
driver.implicitly_wait(5)

intro()

driver.close()

print("BYEEEEEEEEEEE!!!!")