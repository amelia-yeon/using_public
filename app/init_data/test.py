
# 일배치용 공공 데이터 API 사용 test
import requests
import pandas as pd

# key = '6a7655456d616d653939766a59694d'
# url = f'http://openapi.seoul.go.kr:8088/{key}/json/tbLnOpendataRentV/1/2/'

# response = requests.get(url)
# data = response.json()  # dictionary 형태로 가져옴 
# print(data['tbLnOpendataRentV']['row'])



key='6a7655456d616d653939766a59694d'
type='json'
service='tbLnOpendataRentV'
start=1
end=1
                  
url = f'http://openapi.seoul.go.kr:8088/{key}/{type}/{service}/{start}/{end}'
res = requests.get(url)
res_json = res.json()
data = res_json['tbLnOpendataRentV']['row']
print(res_json)
print(data)






# 2022 년도 DATA 적재 - 초기 적재와 같음 
# name = ['ACC_YEAR','SGG_CD','SGG_NM','BJDONG_CD','BJDONG_NM','LAND_GBN','LAND_GBN_NM','BOBN','BUBN',
#         'FLR_NO','CNTRCT_DE','RENT_GBN','RENT_AREA','RENT_GTN','RENT_FEE','BLDG_NM','BUILD_YEAR',
#         'HOUSE_GBN_NM','CNTRCT_PRD','NEW_RON_SECD','CNTRCT_UPDT_RQEST_AT','BEFORE_GRNTY_AMOUNT','BEFORE_MT_RENT_CHRGE']
# file = pd.read_csv('C:\공공데이터\house\서울특별시_전월세가_2022.csv', encoding='cp949',header=None,low_memory=False)
# file.columns = name
# file = file.drop(0, axis=0)
# file.to_csv('C:\공공데이터\house\서울특별시_전월세가_2022_v_utf.csv', index=False, encoding='utf-8')


