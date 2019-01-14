import urllib
import requests
from bs4 import BeautifulSoup
import json

url_base = "http://www.phonecodi.net/front/productlist.php?code="
url_category = {'skin_case': '004',
                'protect_screen': '005',
                'charge/cable': '006',
                'battery/memory': '007',
                'bluetooth/earphone': '008',
                'gender/cradle': '009',
                'string/pen': '010',
                'etc_acc': '011',
                'event_zone': '012'
                }

url_category_sub = {'phone_case': {'soft_case': '001', 'hard_case': '002', 'skin_case': '003'},
                    'protect_screen': '005',
                    'charge/cable': '006',
                    'battery/memory': '007',
                    'bluetooth/earphone': '008',
                    'gender/cradle': '009',
                    'string/pen': '010',
                    'etc_acc': '011',
                    'event_zone': '012'
                    }

url_category_detail = { 'soft_case' : {}

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





