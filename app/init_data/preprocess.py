
import pandas as pd
import os 

# bigquery에 csv 로 바로 로드할 때 (초기 데이터의 경우)
name = ['use_date','line_num','line_name','total_num','take_off_num','register_date']
file = pd.read_csv('C:\공공데이터\CARD_SUBWAY_MONTH_2022.csv', encoding='cp949')
file = file.drop(0, axis=0)
file.to_csv('C:\공공데이터\CARD_SUBWAY_MONTH_2022_v2.csv', index=False, encoding='utf-8')





