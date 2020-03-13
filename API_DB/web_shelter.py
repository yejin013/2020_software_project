from urllib.request import urlretrieve

import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd

# SQLite3 이용
def sqlite_append(shelterDf):
    # C드라이브에 projectDB 폴더 생성 web_shelter.db 파일 생성
    con = sqlite3.connect("c:/projectDB/web_shelter.db")
    shelterDf.to_sql('animalInfo', con, if_exists='append', index=False) # 저장
    con.close()

# 웹 보호소 정보 데이터 파싱 후 sqlite_append 함수 불러오기
def collect_shelter():
    for n in range(1, 30):

        raw = requests.get("http://www.animal.go.kr/portal_rnl/map/mapInfo2.jsp?s_date=&e_date=&s_upr_cd=&"
                           "s_org_cd=&s_up_kind_cd=&s_kind_cd=&s_name=&pagecnt=" + str(n),
                           headers={"User-Agent": "Mozilla/5.0"})
        html = BeautifulSoup(raw.text, 'html.parser')

        # 컨테이너 div.boardArea
        table = html.find('table')

        trs = table.find_all('tr')

        for idx, tr in enumerate(trs):  # enumerate를 사용하면 해당 값의 인덱스를 알 수 있다.
            if idx < 20 and idx % 2 == 1:
                tds = tr.find_all('td')
                area = tds[0].text.strip()  # 앞뒤 여백이 있어 strip()을 사용했다.
                name = tds[1].text.strip()
                tel = tds[2].text.strip()
                addr = tds[3].text.strip()

                # 데이터프레임으로 넣기
                shelter = pd.DataFrame(([[area, name, tel, addr]]),
                    columns=["area", "name", "tel", "addr"])

                # sqlite_append 함수 호출
                sqlite_append(shelter)




# main
collect_shelter()