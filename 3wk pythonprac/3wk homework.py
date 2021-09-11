import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# for문을 돌릴 전체 데이터목록을 가져오기 위해 select로 copy selector에서 공통된 부분을 가져와 변수에 담는다
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# 전체 데이터목록으로 for문을 돌린다. 한 개의 요소들을 하나씩 꺼내 반환하는 for문이기 때문에
# 데이터를 select_one으로 하나씩 가져온다.
for music in musics:
    rank = music.select_one('td.number').text[0:2].strip()
    # 불필요한 순위 상승, 하강 text를 자르기 위해 10의 자리와 1의 자리의 숫자만 표현하고 나머지 문자열을 자를 수 있도록 [0:2] 작성
    title = music.select_one('td.info > a.title.ellipsis').text.strip()
    # 문자열의 공백을 없애기 위해 strip() 함수 사용용    singer = music.select_one('td.info > a.artist.ellipsis').text
    print(rank, title, singer)


