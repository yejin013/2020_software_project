from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import sqlite3
import pandas as pd


# 본인 serviceKey 입력
serviceKey = "key를 입력하세요"


# SQLite3 이용
def sqlite_append(animalDf):
    # C드라이브에 projectDB 폴더 생성 shelter.db 파일 생성
    con = sqlite3.connect("c:/projectDB/api_shelter.db")
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

    # 시 리스트 만들기
    siCode = []

    for item in name:
        siCode.append(item.find("orgcd").text)

    # 시군구 조회
    gungooCode = []

    for i in siCode:
        url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/sigungu?upr_cd=" + \
                   str(i) + "&ServiceKey="
        url = url + serviceKey

        request = urllib.request.urlopen(url)
        xml = request.read()
        soup = BeautifulSoup(xml, "html.parser")

        name = soup.find_all("item")

        for item in name:
            gungooCode.append(item.find("orgcd").text)

    # 보호소 조회
    for i in siCode:
        for j in gungooCode:
            url = "http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/shelter?" \
                  "upr_cd=" + str(i) + "&org_cd=" + str(j) + "&serviceKey="

            url = url + serviceKey

            request = urllib.request.urlopen(url)
            xml = request.read()
            soup = BeautifulSoup(xml, "html.parser")

            name = soup.find_all("item")

            # item에 있는 정보들 불러오기
            for info in name:
                careName = info.find("carenm").text

                # 데이터프레임으로 넣기
                shelter = pd.DataFrame(([[careName]]), columns=["careName"])

                # sqlite_append 함수 호출
                sqlite_append(shelter)





# main
collect_info()
