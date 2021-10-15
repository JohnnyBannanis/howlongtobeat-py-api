import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'accept': '*/*',
    'User-Agent': ua.random
    }

def scraping(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    # Description
    description = soup.find('div', class_= "profile_info large").text.replace("...Read More","")
    description = description.strip()
    # Rating
    li_scrap = soup.find_all('li')
    rating_li = list()
    for i in li_scrap:
        if("Rating" in i.text):
            rating_li.append(i.text)
    rating = rating_li[0]
    # Extra info
    moreInfo = {}
    for i in soup.find_all('div', class_='profile_info'):
        data = i.text.replace("\t","").replace("\n", "")
        splited = data.split(":")
        info_key = splited[0]
        try:
            info_value = splited[1].split(", ")
        except:
            info_value= ""
        if(len(info_value) == 1):
            info_value = info_value[0]
        infoField = [info_key , info_value]
        moreInfo[info_key] = info_value
    info = {
        "description" : description,
        "rating" : rating,
        "game_info" : moreInfo
    }
    return info






