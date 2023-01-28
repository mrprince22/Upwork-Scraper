import json
from urllib.parse import urlencode
import requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time


driver = webdriver.Chrome()

def get_cookies():
    try:
        with open("cookies.json", "r") as f:
            data = json.loads(f.read())    
    except FileNotFoundError:
        return []
    
    cookies = []
    for row in data:
        cookies.append({
             "name": row['name'],
            "value" : row['value']
            })
    
    return cookies


def encoded(keyword):
    keyword = keyword.split()
    keyword = "%20".join(keyword)
    return keyword

def gethtml(keyword = "python", add_cookies = True):
    driver.delete_all_cookies()
    url = "https://www.upwork.com/nx/jobs/search/?q="
    url += encoded(keyword)
    driver.get(url)
    time.sleep(2)
    if add_cookies:
        cookies = get_cookies()
        for cookie in cookies:
            driver.add_cookie(cookie)
    return driver.page_source

