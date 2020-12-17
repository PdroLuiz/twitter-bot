from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import sys

class TwitterBot(webdriver.Chrome):

    def __init__(self, login, password):
        options = Options()
        if 'h' in sys.argv:
            options.add_argument('--headless')
            options.add_argument('--disable-gpu') 
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get("https://www.twitter.com/login")
        self.driver.find_element_by_xpath('//input[@name="session[username_or_email]"]').send_keys(login)
        self.driver.find_element_by_xpath('//input[@name="session[password]"]').send_keys(password)
        self.driver.find_element_by_xpath('//div[@role="button"]').click()

    def home(self):
        self.driver.get("https://www.twitter.com/home")

    def profile(self):
        self.home()
        self.driver.find_element_by_xpath('//a[@aria-label="Profile"]').click()

    def dm(self):
        self.driver.get("https://www.twitter.com/messages")

    def writetweet(self, tweet):
        self.driver.get("https://www.twitter.com/compose/tweet")
        sleep(0.5)
        self.driver.find_element_by_xpath('//div[@aria-label="Tweet text"]').send_keys(tweet)
        self.driver.find_element_by_xpath('//div[@data-testid="tweetButton"]').click()

    def messagerequests(self):
        self.driver.get("https://www.twitter.com/messages/requests")

    def get_new_conversation(self):
        new_messages = self.driver.find_elements_by_xpath('//div[@data-testid="conversation"]')
        return new_messages

    def get_mentions(self):
        self.driver.get("https://www.twitter.com/notifications/mentions")
        sleep(0.5)
    
    def responde_tweet(self, tweet, reply):
        tweet.find_element_by_xpath('//div[@data-testid="reply"]').click()
        sleep(0.5)
        self.driver.find_element_by_xpath('//div[@role="textbox"]').send_keys(reply)
        self.driver.find_element_by_xpath('//div[@data-testid="tweetButton"]').click()

    def listar_tuites(self, assunto, response):
        while True:
            self.driver.get(f"https://www.twitter.com/search?q={assunto}&f=live")
            sleep(2)
            tuites = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
            for tuite in tuites:
                try:
                    tuite.find_element_by_xpath('//div[@data-testid="like"]').click()
                    tuite.find_element_by_xpath('//div[@data-testid="retweet"]').click()
                    sleep(1)
                    self.driver.find_element_by_xpath('//a[@href="/compose/tweet"]').click()
                    sleep(1)
                    self.driver.find_element_by_xpath('//div[@role="textbox"]').send_keys(response)
                    self.driver.find_element_by_xpath('//div[@data-testid="tweetButton"]').click()
                    make()
                except:
                    print('não achou, no caso já retuitou, não fazer nada')

    def reuitar(self, assunto):
        while True:
            self.driver.get(f"https://www.twitter.com/search?q={assunto}&f=live")
            sleep(2)
            tuites = self.driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
            for tuite in tuites:
                try:
                    tuite.find_element_by_xpath('//div[@data-testid="retweet"]').click()
                    sleep(1)
                    tuite.find_element_by_xpath('//div[@data-testid="retweetConfirm"]').click()
                except:
                    pass
                    
                    


