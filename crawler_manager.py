import urllib
import requests
from bs4 import BeautifulSoup
import json

url_base = "http://www.phonecodi.net/front/productlist.php?code="
url_category = {
    '핸드폰 케이스': '004',
    '액정보호 용품': '005',
    '충전기/케이블': '006',
    '배터리/메모리': '007',
    '블루투스/이어폰': '008',
    '충전젠더/거치대': '009',
    '폰줄/목줄/터치펜': '010',
    '기타 악세사리': '011',
    '이벤트존': '012'
}

url_category_sub = {
    '핸드폰 케이스': {'SOFT 케이스': '001', '하드 케이스': '002', '가죽 케이스': '003'},
    '액정보호 용품': '005',
    '충전기/케이블': '006',
    '배터리/메모리': '007',
    '블루투스/이어폰': '008',
    '충전젠더/거치대': '009',
    '폰줄/목줄/터치펜': '010',
    '기타 악세사리': '011',
    '이벤트존': '012'
}

url_category_detail = {
    'SOFT 케이스': {
        '칼라 젤리 케이스': '002',
        '캐릭터 젤리 케이스': '003',
        '투톤 젤리케이스': '005',
        'TPU 강화 이중재질': '007',
        '태블릿 SOFT 케이스': '008',
        '하드 젤리 케이스': '009',
        '미러 젤리 케이스': '011',
        '투명 젤리 케이스': '012',
        '인쇄 젤리 케이스': '013'
    },
    '하드 케이스': {
        '투명 하드케이스': '002',
        'SF 칼라 하드케이스': '003',
        'UV 코팅 하드케이스': '004',
        '범퍼 하드 케이스': '005',
        '일러스트 하드 케이스': '006',
        '프리미엄 하드 케이스': '008',
        '이중재질 하드 케이스': '009',
        '태블릿 하드 케이스': '010',


    }




}

soft_case: ['002', '003', '005', '007', '008', '009', '011', '012', '013']
hard_case: ['002', '003', '004', '005', '006', '008', '009', '010', '013']
skin_case: ['002', '003', '004', '005', '007', '008', '010']



#temp = url_category_sub.get('phone_case')[1]

for i in url_category.keys():
    print(i)
    print(url_category.get(i))
    print(url_category_sub.get(i))
    print()
    #for j in url_category_
    detail = url_category_sub[i]
    #print(url_category_detail[detail])





#url = url1 + url2['phone_case'] + url3['hard_case']

#html = requests.get(url).text
#soup = BeautifulSoup(html, "html.parser")
#print(soup)

"""
#가져올 상품 데이터 종류 목록
exist =
category = 
product_name =
thumnail_img_link =
detail_img_link = 
consumer_price = 
sell_price = 
product_code =
manufacturer = 
brand = 
origin = 
revise = 
option1 = 
option2 = 
option3 =
option4 = 
option5 = 
option6 = 
option7 = 
option8 = 
option9 = 
option10 =
"""





