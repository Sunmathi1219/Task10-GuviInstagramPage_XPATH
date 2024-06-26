"""
Using Python selenium automation and the URL https://www.instagram.com/guviofficial/ kindly do the following mentioned
tasks:
1.)Use either relative or absolute xpath only for the task
2.)Extract the total number of followers and following from the URL mentioned above
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Guvi_InstagramPage:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #Fetch the URL
    def get_url(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            print(self.driver.current_url)
            print(self.driver.title)
            sleep(5)

            return True

        except Exception as e:
            print(e)
            return False
    # Total Number of followers from the URL
    def extract_followers(self):
        followers_xpath="//ul[@class='x78zum5 x1q0g3np xieb3on']//li[2]//div//button//span//span"
        followers_element = self.driver.find_element(by=By.XPATH,
                                                     value=followers_xpath)
        sleep(2)

        print("Total Number Of Followers :", followers_element.text)
        return True

    #Total Number Of Following From The URL
    def extract_following(self):
        following_xpath="//ul[@class='x78zum5 x1q0g3np xieb3on']//li[3]//div//button//span//span"
        following_element=self.driver.find_element(by=By.XPATH, value=following_xpath)
        sleep(2)

        print("Total Number Of Following :", following_element.text)
        return True

    def shutdown(self):
        self.driver.quit()
        return None



"""
if __name__ == "__main__":
    instagram_Page = Guvi_InstagramPage("https://www.instagram.com/guviofficial/")
    print(instagram_Page.get_url())
    instagram_Page.extract_followers()
    instagram_Page.extract_following()
    instagram_Page.shutdown()
"""