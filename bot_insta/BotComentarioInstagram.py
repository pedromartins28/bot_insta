from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time
import random


PROXY = '192.168.0.67'
PROXY_PORT = '139'

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        firefoxProfile.set_preference("network.proxy.type", 1)
        firefoxProfile.set_preference("network.proxy.type", PROXY)
        firefoxProfile.set_preference("network.proxy.type", PROXY_PORT)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"./geckodriver"
        )

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        user_element = driver.find_element("xpath",
        
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element("xpath",
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(10)
        driver.get("post")
        time.sleep(5)
        comentarios = [""]

        driver.find_element("xpath", "//textarea[@class='x1i0vuye xvbhtw8 x76ihet xwmqs3e x112ta8 xxxdfa6 x5n08af x78zum5 x1iyjqo2 x1qlqyl8 x1d6elog xlk1fp6 x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd xtt52l0 xnalus7 xs3hnx8 x1bq4at4 xaqnwrm']").click()
        i=1;
        while(1):
            time.sleep(5)
            random_coment = random.choice(comentarios)
            print("Digitando...")
            for letter in random_coment:
                driver.find_element("xpath", "//textarea[@placeholder='Adicione um comentário...']").send_keys(letter)
                time.sleep(random.randint(1, 5)/30)
            time.sleep(5)
            driver.find_element("xpath", "//div[@class='x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x1ypdohk x1i0vuye x1f6kntn xwhw2v2 xl56j7k x17ydfre x2b8uid xlyipyv x87ps6o x14atkfc x1d5wrs8 xjbqb8w xm3z3ea x1x8b98j x131883w x16mih1h x972fbf xcfux6l x1qhh985 xm0m39n xt0psk2 xt7dq6l xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x1n5bzlp x173jzuc x1yc6y37']").click()
            print(str(i) + " comentários enviados com sucesso!")
            i=i+1
            time.sleep(1)
            print("Aguardando alguns minutos...")
            time.sleep(random.randint(22, 77))













InstagramBot("user", "pass").login()
