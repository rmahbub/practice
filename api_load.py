import pandas as pd
from pandas import DataFrame
import requests
import simplejson as json
from datetime import datetime, date, timedelta



def get_data(ticker):

	#ticker= str(ticker)
	url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=%s&apikey=PVJM7WDANY5628ZC'%ticker
	#api_key = 'c5tcNhXmViUZrkVx5M5A'
	today = date.today()
	today_string=today.strftime("%Y-%m-%d")
	start_date = today.replace(year=today.year if today.month > 1 else today.year - 1, month=today.month - 1 if today.month >1 else 12)
	start_date_string=start_date.strftime("%Y-%m-%d")
	start = start_date
	end = today
	daterange = [start + timedelta(days=x) for x in range(0, (end-start).days)]
	date_strings = [dt.strftime("%Y-%m-%d") for dt in daterange]
	#final_url = url + "&start_date=" + start_date_string + "&end_date=" + today_string + "&api_key=" + api_key
	resp = requests.get(url)
	json = resp.json()
	TimeSeries=json['Time Series (Daily)']
	data1 = dict((k, TimeSeries[k]['4. close']) for k in date_strings if k in TimeSeries)
	#dataset=json['dataset']
	#data=dataset['data']
	temp = []
	data = []
	for key, value in data1.items():
		temp = [key,value]
		data.append(temp)
	df = DataFrame(data)
	df[1] = pd.to_numeric(df[1])
	try:
		df = df.set_index(0)
		df.index = pd.to_datetime(df.index)
		df.columns = ['closing']
		return df
	except Exception as e:
		df = []
		return df
