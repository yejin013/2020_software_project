import requests
from bs4 import BeautifulSoup
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import sqlite3
import pandas as pd


# 본인 serviceKey 입력
serviceKey = "718617iI2GVV0AWrip1dEkJMt3Jl9GPvl%2Flz28ktLjA7EYSXhYwCFjFlH9LovIRqzDDkAeUy29%2FaugkKim%2Fa%2Fw%3D%3D"


# SQLite3 이용
def sqlite_append(animalDf):
    # C드라이브에 projectDB 폴더 생성 animalInfo.db 파일 생성
    con = sqlite3.connect("c:/projectDB/animalInfo.db")
    animalDf.to_sql('animalInfo', con, if_exists='append', index=False) # 저장
    con.close()


# API 데이터 파싱 후 sqlite_append 함수 불러오기
def collect_info():
    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey="
    url = url + serviceKey

    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, "html.parser")
    # name = soup.find_all("item")

    totalCount = soup.find("totalcount").text

    # 고양이만
    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?" \
            "&numOfRows=" + totalCount + "&upkind=422400" + "&ServiceKey="
    url = url + serviceKey

    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, "html.parser")

    item = soup.find_all("item")

    # item에 있는 정보들 불러오기
    for info in item:
        careaddr = info.find("careaddr").text
        carenm = info.find("carenm").text
        caretel = info.find("caretel").text
        kindcd = info.find("kindcd").text
        happendt = info.find("happendt").text
        happenplace = info.find("happenplace").text
        specialmark = info.find("specialmark").text
        poster_src = info.find("popfile").text

        # 검색할 주소
        location = careaddr

        # Production(실제 서비스) 환경 - https 요청이 필수이고, API Key 발급(사용설정) 및 과금 설정이 반드시 필요합니다.
        URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyCAQHutKTDQok1dWeNv8jO73HcZpcyHgqo' \
              '&sensor=false&language=ko&address={}'.format(location)

        # URL로 보낸 Requst의 Response를 response 변수에 할당
        response = requests.get(URL)

        # JSON 파싱
        data = response.json()

        # lat, lon 추출
        if (data['results'][0]['geometry']['location']['lat']):
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']
        else:
            location = carenm

            # Production(실제 서비스) 환경 - https 요청이 필수이고, API Key 발급(사용설정) 및 과금 설정이 반드시 필요합니다.
            URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyCAQHutKTDQok1dWeNv8jO73HcZpcyHgqo' \
                  '&sensor=false&language=ko&address={}'.format(location)

            # URL로 보낸 Requst의 Response를 response 변수에 할당
            response = requests.get(URL)

            # JSON 파싱
            data = response.json()

            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']

        # 데이터프레임으로 넣기
        animalInfo = pd.DataFrame(([[careaddr, carenm, caretel, kindcd, happendt, happenplace, specialmark, lat, lng, poster_src]]),
                                  columns=["careaddr", "carenm", "caretel", "kindcd", "happendt", "happenplace",
                                           "specialmark", "lat", "lng", "poster_src"])

        # sqlite_append 함수 호출
        sqlite_append(animalInfo)





# main
collect_info()