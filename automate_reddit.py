from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

def join(driver):
    try:
        join_button = driver.find_element('xpath','//*[@id="AppRouter-main-content"]/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/button')
        if join_button.text == 'Join':
            join_button.click()
            time.sleep(1)
        else:
            print("Already Joined")
    except NoSuchElementException:
        print("Join Button Not Found")

def start_automation(driver):
    with open("subreddit_list.txt", "r") as reddit_list:
        for line in reddit_list:
            print(f"Opening....{line}")
            driver.get(f"https://www.reddit.com{line}")
            try:
                eighteen_plus = driver.find_element('xpath','//*[@id="AppRouter-main-content"]/div/div[1]/div/div/div[2]/button')
                eighteen_plus.click()
            except NoSuchElementException:
                print("18+ not_required...")
                join(driver)

if __name__ == "__main__":
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # Please run chrome using following command in cmd. and log in into reddit so that session is saved
    # path/to/chrome.exe --remote-debugging-port=8080 --user-data-dir="C:\selenium\ChromeProfile"
    # following port localhost:8080 and --remote-debugging-port=8080, should always use same port
    # make sure to create a folder to save your session and specify it with --user-data-dir
    options.add_experimental_option("debuggerAddress", "localhost:8080")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    start_automation(driver)
    driver.close()