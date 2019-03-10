import pandas as pd
from pandas import DataFrame
import requests
import simplejson as json
from datetime import datetime, date



def get_data(ticker):

#ticker='HD'
url = 'https://www.quandl.com/api/v3/datasets/EOD/%s?column_index=4'%ticker
api_key = 'c5tcNhXmViUZrkVx5M5A'

today = date.today()
today_string=today.strftime("%Y-%m-%d")
start_date = today.replace(year=today.year if today.month > 1 else today.year - 1, month=today.month - 1 if today.month >1 else 12)
start_date_string=start_date.strftime("%Y-%m-%d")
final_url = url + "&start_date=" + start_date_string + "&end_date=" + today_string + "&api_key=" + api_key

dataser=json['dataset']
data=dataset['data']
df=DataFrame(data)
try:
        df = df.set_index(0)
        df.index = pd.to_datetime(df.index)
      #  df.columns = ['closing']
        return df
    except Exception as e:
        df = []
        return df