from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time

def getLocation():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--use--fake-ui-for-media-stream")
    driver = webdriver.Chrome(executable_path='C:/Users/hrishabh/PycharmProjects/Acurate Geolocation/chromedriver.exe', options=options)
    # Store chromedriver.exe in ur python file location itself
    # Edit the path accordingly
    
    #Wait Time to load the page
    timeout = 20
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    
    longitude = driver.find_elements_by_xpath('//*[@id="latitude"]')  # Replace with any XPath //*[@id="latitude"]
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    
    latitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    
    driver.quit()
    return (latitude, longitude)
