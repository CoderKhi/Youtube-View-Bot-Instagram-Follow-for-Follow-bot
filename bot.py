import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

print("Incase you do not have selenium intalled, we are installing it for you!")
os.system("pip install selenium")
os.system("pip3 install selenium")
class YoutubeBot():
    def __init__(self, viewAmount, watchTimeAmount, URL):
        self.vam = viewAmount, self.wta = watchTimeAmount, self.url = URL
        self.driver = webdriver.Chrome("your path");
        self.driver.get(self.url);

        for i in range(int(self.vam)):
            print("Loading page...");
            time.sleep(4);
            for _ in range(int(self.wta)):
                time.sleep(1);
                print("[+]1 second of watch time added.");
                self.driver.refresh();
class InstagramBot():
    def __init__(self, followAmount, username, password):
        self.famo = followAmount, self.username = username, self.password = password
        self.driver = webdriver.Chrome("your path");
        self.driver.get("https://www.instagram.com/explore/people/suggested/");
        usernameField = self.driver.find_element_by_name("username");
        usernameField.send_keys(self.username);
        passwordField = self.driver.find_element_by_name("password");
        passwordField.send_keys(self.password);
        loginButton = self.driver.find_element_by_xpath("//*[@id=\"loginForm\"]/div/div[3]");
        loginButton.click()
        followButtons = self.driver.find_element_by_link_text("Follow")
        for x in range(int(self.famo)):
            print("Loading page...");
            time.sleep(4)
            for _ in range(int(self.famo)):
                time.sleep(0.7)
                followButtons.click()
                print("[+]1 person followed.")

            
print("1: Youtube View bot");
print("2: Instagram Follow For Follow bot");
selection = int(input("enter your choice."));

if (selection == 1):
    bot = YoutubeBot(100, 40, "https://youtube.com");
elif (selection == 2):
    bot = InstagramBot(100, "username here", "password here")
