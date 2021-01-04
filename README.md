# 2020_software_project
## 프로젝트명 : 고영희 찾기

### 1. 프로젝트의 개요
#### 1-1. 프로젝트 개발 배경
&nbsp;&nbsp;&nbsp;길거리를 지나다니다 보면 종종 반려동물을 찾는다는 전단지를 볼 수 있다. 그들 중 반려동물을 찾는 사람도 있지만 그런 노력에도 불구하고 찾지 못하는 경우도 있다. 본 프로그램 <고영희 찾기>는 ‘잃어버린 반려동물을 어떻게 하면 빠르게 찾아줄 수 있을까?’라는 고민에서 고안되었다.  
&nbsp;&nbsp;&nbsp;[그림 1]에서 볼 수 있듯이 유기/유실된 동물은 원 소유주 반환 및 공고 기간이 7-10일이며 이 기간이 지나면 동물의 소유권은 지자체로 넘어간다. 즉 7-10일 안에 반드시 반려동물을 찾아내야한다. 하지만 원래 주인에게 돌아가는 비율은 현저히 낮다. [그림 2]에서도 볼 수 있듯이 원래 주인에게 인도되는 비율이 평균 15.1%에 불과하고 특히 고양이의 경우 1.57%에 불과하다.  
&nbsp;&nbsp;&nbsp;고양이의 경우 현재 반려동물 등록제의 의무 대상이 아니기 때문에 발견이 되어도 주인을 빠르게 찾아주기 어렵다. 또한 경계심이 강하고 예민해 보호소로 옮겨져도 자연사하는 비율이 41.8%로 개가 15.5%에 비하면 현저히 높은 것을 알 수 있다. 이러한 이유로 고양이의 경우 빠르게 원래 주인을 찾아주는 것이 가장 바람직하다. 따라서 본 팀은 인도 비율이 가장 낮은 고양이를 원래 주인에게 빠르게 찾아주기 위해 <고영희 찾기>를 개발한다.  

<p align="center" style="color:gray">
  [그림 1] 유기동물 처리 체계도<br>
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/44939208/103543456-e6b28780-4ee1-11eb-9a37-d7bec2c6c112.png" alt="유기동물 처리 체계도" width="50%" height="50%"  />
</p> 

<p align="center" style="color:gray">
  [그림 2] 연도별 주인에게 인도되는 비율<br>
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/44939208/103543521-0053cf00-4ee2-11eb-9c15-d2d5c146fc7e.png" alt="연도별 인도 비율" width="50%" height="50%"  />
</p> 

#### 1-2. 프로젝트 최종 목표
#### 최종 목표 : AI 기술을 이용해 주인에게 유실묘를 최대한 빠르게 찾아주는 것을 주요 목적으로 한다. 

#### 세부 목표
- 웹 서비스 구현 :  
&nbsp;&nbsp;&nbsp;사용자가 고양이를 쉽게 찾고 고양이가 쉽게 주인을 찾을 수 있도록 공고, 검색, 자체 실종신고 및 발견신고 게시판, 사용자 주변 보호소 조회 등의 기능을 제공한다. 또한 사용자가 이러한 기능을 쉽게 사용하도록 웹 서비스를 제공한다.

- 크롤링을 이용한 보호소의 공고 정보 제공 기능 구현 :  
&nbsp;&nbsp;&nbsp;정부가 제공하는 공공데이터 포털에서 제공하는 ‘동물보호관리시스템 유기동물 조회 서비스’를 이용해 유기된 고양이 데이터(보호소 이름, 위치, 전화번호, 발견 장소, 특징, 이미지)를 가져와 사용자에게 제공한다.

- 지도 API를 이용한 주변 보호소 정보 기능 구현 :  
&nbsp;&nbsp;&nbsp;'Google Geocoding API', ‘Google Maps Geolocation API’와 ‘kakao maps API’를 이용해 사용자 주변 보호소의 위치를 보여주고 보호소 관련 정보를 제공한다. 이때, 주변 보호소 정보는 '동물보호관리시스템' 웹사이트에서 동물보호센터 정보를 웹크롤링하여 가져온다.

- 머신러닝을 이용한 검색 서비스 구현 :  
&nbsp;&nbsp;&nbsp;구글의 ‘Teachable Machine’을 이용해 고양이 품종을 찾아내는 머신러닝 모델을 생성해낸다. 이 모델을 이용하여 검색 시 사용자가 제공하는 고양이 이미지의 품종을 분석해내고 찾아낸 품종과 관련된 고양이 공고를 제공한다.

### 2. 개발 환경 및 개발 언어
|| tool |
| ------ | ------ |
| 개발언어 | ![issue badge](https://img.shields.io/badge/python-3.7.4-blue.svg) ![issue badge](https://img.shields.io/badge/javascript-blue.svg) |
| 라이브러리 & 프레임워크 | ![issue badge](https://img.shields.io/badge/Django-3.0.3-green.svg) ![issue badge](https://img.shields.io/badge/jQuery-green.svg) ![issue badge](https://img.shields.io/badge/Bootstrap-green.svg) |
| Open API | [동물보호관리시스템 유기동물 조회 서비스 API](https://www.data.go.kr/data/15001096/openapi.do) |
| 개발환경 | Windows10 |
| 데이터베이스 환경 | ![issue badge](https://img.shields.io/badge/SQL-sqlite-lightgrey.svg) |

### 3. 시스템 구조도

&nbsp;본 프로젝트의 구조도는 [그림 3]과 같다. 아래의 표는 주요 모듈의 세부 설명이다.

<p align="center" style="color:gray">
  [그림 3] 시스템 구조도<br>
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/44939208/103543700-4dd03c00-4ee2-11eb-961b-87ee655e41cc.png" alt="구조도" width="50%" height="50%"  />
</p> 
 
| 모듈명 | 역할 |
| ------ | ------ |
| home | 웹 페이지의 홈 화면을 보여준다. |
| login | 댓글, 쪽지를 이용하기 위하여 로그인/회원가입을 기능을 구현하였다. |
| mypage | 비밀번호 변경, 연락처 수정 등 개인정보를 수정할 수 있다. 사용자가 작성했던 게시글을 확인할 수 있다. 또한 쪽지 쓰기 및 회원 간 주고받은 쪽지를 관리할 수 있다. |
| post | 발견동물 게시판 / 실종동물 게시판의 게시글 보기, 게시글 수정, 게시글 삭제, 댓글 기능을 담당한다. |
| shelter | Google Geocoding API, Google Maps Geolocation API와 카카오 지도 API을 이용하여 사용자의 위치 지도와 주변 보호소 정보 및 지도를 볼 수 있다. |
| develop | 티처블 머신을 이용하여 고양이 품종을 분류한 후, 가장 높은 정확도를 보이는 품종의 고양이 정보를 보여준다. |
  
### 4. 고영희 찾기 웹 화면 일부
  
<p align="center" style="color:gray">
  [그림 4] 고영희 찾기 메인 화면 <br>
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/44939208/103544493-84f31d00-4ee3-11eb-872f-58a436307655.png" alt="메인 화면" width="50%" height="50%"  />
</p> <br>

<p align="center" style="color:gray">
  [그림 5] 사진 업로드 <br>
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/44939208/103544478-80c6ff80-4ee3-11eb-9db7-ae1be0cb1235.png" alt="사진 업로드" width="50%" height="50%"  />
</p> <br>

<p align="center" style="color:gray">
  [그림 6] 품종 분류 결과 페이지 <br>
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/44939208/103544469-7d337880-4ee3-11eb-80e1-36e89a04c584.png" alt="품종 분류 결과" width="50%" height="50%"  />
</p> <br>

<p align="center" style="color:gray">
  [그림 7] 주변보호소정보 <br>
  <img style="margin:50px 0 10px 0" src="https://user-images.githubusercontent.com/44939208/103544467-7c024b80-4ee3-11eb-8ed7-09c471f477c4.png" alt="주변보호소정보" width="50%" height="50%"  />
</p> <br>

-----------------
## 프로젝트 기간
2020.02.01 - 2020.06.19

## Contributor
+ 팀명 : 강형욱팀
+ 팀장 : 숭실대학교 소프트웨어학부 이아현 (Front-End, 머신러닝)
+ 팀원 : 숭실대학교 소프트웨어학부 박수현 (Front-End, 머신러닝)
+ 팀원 : 숭실대학교 소프트웨어학부 진혜원 (Back-End, 머신러닝)
+ 팀원 : 숭실대학교 소프트웨어학부 채예진 (Back-End, 머신러닝)