import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.gxzsir3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

genie = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for genies in genie:


    rank = genies.select_one('td.number').text
    title = genies.select_one('td.info > a.title.ellipsis').text
    artist = genies.select_one('td.info > a.artist.ellipsis').text

    print(rank[0:2].rstrip()+' '+ title.lstrip() + ' '+artist)




