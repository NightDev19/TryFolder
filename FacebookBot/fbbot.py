from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import bs4
from bs4 import BeautifulSoup as soup 
from urllib.request import Request, urlopen
from time import sleep
import pyautogui


#fetching hashtags

def hashtags(hash_idea):
    url = 'http://best-hashtags.com/hashtag/' + hash_idea

    try:
        req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
        page = urlopen(req, timeout=10)
        page_html = page.read()
        page.close()
        page_soup = soup(page_html, 'html.parser')
        result = page_soup.find('div',{'class':'tag-box tag-box-v3 margin-bottom-40'})
        tags = result.decode()
        start_index = tags.find('#')
        end_index = tags.find('</p1>')
        tags = tags[start_index:end_index]

        return tags
    except:
        print('Something went wrong While Fetching hashtags')


def login(username, password):

    try:
        url = 'https://facebook.com'
        driver.get(url)
        user = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'email')))
        user.send_keys(username)
        pas = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME, 'pass')))
        pas.send_keys(password)
        login_btn = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.NAME,'login')))
        login_btn.click()

    except:
        print('Something went wrong while login process')

def upload(img_path,caption):
    try:
        btn1 = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[3]/span/div/i')))
        btn1.click()
        btn2 = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div[2]/div[1]/div/div[1]')))
        btn2.click()
        btn3= WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[1]/div[2]/div/div[1]/span/div/div/div/div/div[1]/i')))
        btn3.click()
        pyautogui.write(img_path)
        pyautogui.press('enter')
        cap = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div')))
        cap.send_keys(caption)
        sleep(5) # this is mandatory while doing some thing with bot
        btn_post = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[10]/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]/div/span/span')))
        btn_post.click()
    except:
        print('Something Went Wrong While posting the image or video')
if __name__== "__main__":
    #turn for credentials, driver, and caption
    username = input('ENTER USERNAME : ')
    password = input('ENTER PASSWORD : ')
    img_path = input('Enter Image Path : ')
    hash_idea = input('ENTER ONE HASH : ')
    caption = input('ENTER CAPTION : ') # if you want to
    caption = caption + '\n' , hashtags(hash_idea)
    driver = webdriver.Chrome()
    login(username,password)
    upload(img_path,caption)