print('##################  외부 module  ##################')

# 모듈 설치
# pip install 모듈이름
# pip install 모듈이름==0.0
# pip install beautifulsoup4 (in terminal)
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# 사용
html_doc = """
    <html>
        <head>
            <title>TEST PAGE</title>
        </head>
        <body>
            <h1>HELLO WORLD</h1>
        </body>
    </html>
"""
from urllib import request
from bs4 import BeautifulSoup

conent = request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
# soup = BeautifulSoup(html_doc, 'html.parser')
soup = BeautifulSoup(conent, 'html.parser')

# print(soup.select("data"))

# 3 개만 찍어보자..
i = 0
for data in soup.select("data"):    
    if i < 3:
        print("시간:", data.select_one("tmef").string, " 날씨:" , data.select_one("wf").string)
        print("-" * 20)
        i += 1



