from urllib.request import urlretrieve
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
    con = sqlite3.connect("c:/projectDB/animalInfo.db")
    animalDf.to_sql('animalInfo', con, if_exists='append', index=False) # 저장
    con.close()


# API 데이터 파싱 후 sqlite_append 함수 불러오기
def collect_info():
    # 시도 조회(시도는 17개)
    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sido?numOfRows=17&ServiceKey="
    url = url + serviceKey

    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, "html.parser")
    name = soup.find_all("item")

    # 시도 입력받기(어떻게 입력받게 할까?? 웹에서 선택)
    si = "서울특별시"

    for item in name:
        if si == item.find("orgdownnm").text:
            siCode = item.find("orgcd").text

    # 시군구 조회
    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sigungu?upr_cd=" + \
          siCode + "&ServiceKey="
    url = url + serviceKey

    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, "html.parser")

    name = soup.find_all("item")

    # 시군구 입력받기
    gu = "강동구"

    for item in name:
        if gu == item.find("orgdownnm").text:
            guCode = item.find("orgcd").text

    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?" \
          "upr_cd=" + siCode + "&org_cd=" + guCode + "&ServiceKey="
    url = url + serviceKey

    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, "html.parser")

    # 페이지 수가 여러개인 것들을 위하여 한 페이지에 모든 데이터 받아오기(코드 줄이기 위하여)
    totalCount = soup.find("totalcount").text

    url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?" \
            "upr_cd=" + siCode + "&org_cd=" + guCode + "&numOfRows=" + totalCount + "&ServiceKey="
    url = url + serviceKey
    print(url)

    request = urllib.request.urlopen(url)
    xml = request.read()
    soup = BeautifulSoup(xml, "html.parser")

    item = soup.find_all("item")

    # item에 있는 정보들 불러오기
    for info in item:
        age = info.find("age").text
        careaddr = info.find("careaddr").text
        carenm = info.find("carenm").text
        caretel = info.find("caretel").text
        colorcd = info.find("colorcd").text
        kindcd = info.find("kindcd").text
        specialmark = info.find("specialmark").text
        # poster_src = info.find("popfile").text
        # urlretrieve(poster_src, "popfile/" + careaddr[:4] + ".png")

        # 데이터프레임으로 넣기
        animalInfo = pd.DataFrame(([[age, careaddr, carenm, caretel, colorcd, kindcd, specialmark]]),
                                columns=["age", "careaddr", "carenm", "caretel", "colorcd", "kindcd",
                                               "specialmark"])

        # sqlite_append 함수 호출
        sqlite_append(animalInfo)





# main
collect_info()