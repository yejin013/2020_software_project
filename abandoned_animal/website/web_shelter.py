from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd
from django.shortcuts import render

from .models import ShelterInformation

# SQLite3 이용
def sqlite_append(shelterDf):
    # C드라이브에 projectDB 폴더 생성 web_shelter.db 파일 생성
    con = sqlite3.connect("c:/projectDB/web_shelter.db")
    shelterDf.to_sql('animalInfo', con, if_exists='append', index=False) # 저장
    con.close()

# 웹 보호소 정보 데이터 파싱 후 sqlite_append 함수 불러오기
def collect_shelter():

    # 보호소 개수 파악
    raw = requests.get("https://www.animal.go.kr/front/awtis/institution/institutionList.do?menuNo=1000000059",
                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')
    total = html.select_one('div.boardList2 ul')

    raw = requests.get("https://www.animal.go.kr/front/awtis/institution/institutionList.do?pageSize=" + str(total.text[2:-2]),
                       headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너 div.boardArea
    table = html.select('div.boardList2 table tbody tr')

    for tr in table:
        tds = tr.find_all('td')
        area = tds[0].text.strip()  # 앞뒤 여백이 있어 strip()을 사용했다.
        name = tds[1].text.strip()
        tel = tds[2].text.strip()
        addr = tds[3].text.strip()

        # 검색할 주소
        location = addr

        # Production(실제 서비스) 환경 - https 요청이 필수이고, API Key 발급(사용설정) 및 과금 설정이 반드시 필요합니다.
        URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyCAQHutKTDQok1dWeNv8jO73HcZpcyHgqo' \
              '&sensor=false&language=ko&address={}'.format(location)

        # URL로 보낸 Requst의 Response를 response 변수에 할당
        response = requests.get(URL)

        # JSON 파싱
        data = response.json()

        # lat, lon 추출
        if(data['results'][0]['geometry']['location']['lat']):
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
        else:
            location = name

            # Production(실제 서비스) 환경 - https 요청이 필수이고, API Key 발급(사용설정) 및 과금 설정이 반드시 필요합니다.
            URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyCAQHutKTDQok1dWeNv8jO73HcZpcyHgqo' \
                  '&sensor=false&language=ko&address={}'.format(location)

            # URL로 보낸 Requst의 Response를 response 변수에 할당
            response = requests.get(URL)

            # JSON 파싱
            data = response.json()

            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']

        ShelterInformation(name=name, address=addr, phone=tel, area=area, lat=lat, lng=lng).save()

'''
shelter = pd.DataFrame(([[area, name, tel, addr, lat, lng]]),
                               columns=["area", "name", "tel", "addr", "latitude", "longitude"])

        # sqlite_append 함수 호출
        sqlite_append(shelter)
'''


def shelterDB(request):
    collect_shelter()
    return render(request, 'db.html')