import yaml
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]



class Site:
    def __init__(self, address):
        if browser == 'firefox':
            services = Service(executable_path=GeckoDriverManager().install())
            option = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(service=services, options=option)
        elif browser == 'chrome':
            services = Service(executable_path=ChromeDriverManager().install())
            option = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=services, options=option)
        self.driver.implicitly_wait(testdata['implicitly_wait'])
        self.driver.maximize_window()
        self.driver.get(address)
        time.sleep(testdata["sleep_time"])

    def find_element(self, mode, path):
        if mode == "css":
            element = self.driver.find_element(By.CSS_SELECTOR, path)
        elif mode == "xpath":
            element = self.driver.find_element(By.XPATH, path)
        else:
            element = None
        return element

    def get_element_property(self, mode, path, property):
        element = self.find_element(mode, path)
        return element.value_of_css_property(property)

    def close(self):
        self.driver.close()
