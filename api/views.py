#ChangeLog
#Version 1.0.0 -- Jayesh
#	--- Adding Basic Functions for the API's

# path('/dailyprice',views.dailyprice,name='index'),
# 	path('/activateprice',views.activateprice),
# 	path('/crop-price',views.cropprice), 


from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from django.db import connection
from datetime import datetime, timedelta
import tabula
from api.models import DailyPrice,DailyPriceLog
import pickle
import time 
import sklearn
import os
# Create your views here.


def index(request):
	return HttpResponse("Hello Farmos")

def dailyprice(request):
	#fetch the code from sqlite3 database
	#add the data to the list
	#append the list to a dictionary
	#return the dictionary

	result = [] #result list 
	all_prices = DailyPrice.objects.all();
	daily_price_dict = {'name':'Onion','measure':'Quintal','min_price':10,'max_price':12,'avg_price':11,'commodity_number':4062}
	# result.append(daily_price_dict)
	final_result = {'date':'02 February 2021','size':len(all_prices),'result':result}
	
	for obj in all_prices: 
		new_dict = {'name':obj.name,'measure':obj.measure,'commodity_number':obj.commodity,'arrival':obj.arrival,'min_price':obj.min_price,'max_price':obj.max_price,'avg_price':obj.avg_price}
		result.append(new_dict)

	final_result['result'] = result
	return JsonResponse(final_result)
	# return HttpResponse(dfs[0].head())
	# return FileResponse(open(url, 'rb'), content_type='application/pdf')

def activateprice(request):
	#check the user credentials
	#fire the wget function 
	#check if the file is stored with price-date.pdf
	#start tabula.py
	#truncate the current-daily-price table
	#add the new values to the table
	#return finish
	with connection.cursor() as cursor: 
		cursor.execute("DELETE FROM api_dailyprice")

	url = staticfiles_storage.path('dailyrates.pdf')
	x = datetime.now()
	date = x.strftime("%d %B %Y")
	# TABULA PY CODE 

	dfs = tabula.read_pdf(url,stream=True,pages="all")
	lst = []
	max_page = len(dfs)
	for dfs_l in range(0,len(dfs)):
		for index, row in dfs[dfs_l].iterrows():
			if "CommodityA_Crroivdael Arrival_Unit" in row:
				r = row['CommodityA_Crroivdael Arrival_Unit']
				x = r.split(" ")
				commodity_name = row['Commo_Desc']
				if(type(commodity_name) == type("str") and len(x) > 2):
					database_dailyprice = DailyPrice(name=commodity_name,commodity=x[0], measure = x[2], arrival = x[1], min_price=row['Min_Rate'],max_price=row['Max_Rate'],avg_price=row['Avg_Rate'])
					database_dailyprice.save()
			else:
				if("CommodityA_Crroidveal" in row):
					r = row['CommodityA_Crroidveal']
				else: 
					r = row["CommodityA_Crroivdael"]
				commodity_name = row['Commo_Desc']
				qtl = row['Arrival_Unit']
				if(type(r) == type(1)):
					if(type(commodity_name) == type("str")):
						comm = r
						measure_x = row['Unnamed: 0']
						database_dailyprice = DailyPrice(name=commodity_name,commodity=comm, measure = qtl, arrival = measure_x, min_price=row['Min_Rate'],max_price=row['Max_Rate'],avg_price=row['Avg_Rate'])
						database_dailyprice.save()
					else:
						x = r.split(" ")
						commodity_name = row['Commo_Desc']
						if(type(commodity_name) == type("str") and len(x) > 1):
							database_dailyprice = DailyPrice(name=commodity_name,commodity=x[0], measure = qtl, arrival = x[1], min_price=row['Min_Rate'],max_price=row['Max_Rate'],avg_price=row['Avg_Rate'])
							database_dailyprice.save()



				

		    # obj['name'] = commodity_name
		    # obj['avg_price'] = row['Avg_Rate'] 
		    # obj['min_price'] = row['Min_Rate']
		    # obj['max_price'] = row['Max_Rate']
		    # obj['commodity_number'] = x[0]
		    # obj['arrival'] = x[1]
		    # obj['measure'] = x[2]

	database_dailypricelog = DailyPriceLog(date=date,result="success")
	database_dailypricelog.save();

	return JsonResponse({'result':'success'})


def cropprice(request):
	#this particular function will take 3 values
	#from date
	#to date
	#crop name
	# These 3 parameters will be passed on to the model 
	# the model will return the crop price prediction for 7 days 
	# only for 10 valid crops 
	# return type will be JsonResponse
	response = {}
	response['success'] = True
	response['onion'] = []
	response['potato'] = []
	response['garlic'] = []
	response['methi'] = []
	unix = int(time.time())
	date_list = [unix]
	for i in range(2,8):
		date_list.append(unix + 86400*i)
	onion = os.path.join(os.path.dirname(__file__), 'onion.sav')
	potato = os.path.join(os.path.dirname(__file__), 'potato.sav')
	garlic = os.path.join(os.path.dirname(__file__), 'garlic.sav')
	methi = os.path.join(os.path.dirname(__file__), 'methi.sav')
	model = pickle.load(open(onion,'rb'))
	model2 = pickle.load(open(potato,'rb'))
	model3 = pickle.load(open(garlic,'rb'))
	model4 = pickle.load(open(methi,'rb'))
	final_ans = []
	final_ans_p = []
	final_ans_g = []
	final_ans_m = []

	for x in date_list:	
		k = model.predict([[x,100]])
		l = model2.predict([[x,100]])
		m = model3.predict([[x,100]])
		o = model4.predict([[x,100]])
		final_ans.append(k[0].tolist())
		final_ans_p.append(l[0].tolist())
		final_ans_g.append(m[0].tolist())
		final_ans_m.append(o[0].tolist())
	final_r = []
	final_p = []
	final_g = []
	final_m = []

	d = 0
	presentday = datetime.now()
	for y in final_ans:
		date = presentday + timedelta(d)
		temp = {}
		temp['date'] = date.strftime('%d-%m-%Y')
		temp['min_price'] = y[0]
		temp['max_price'] = y[1]
		temp['avg_price'] = y[2]
		final_r.append(temp)
		d = d +1 
	d = 0
	for y in final_ans_p:
		date = presentday + timedelta(d)
		temp = {}
		temp['date'] = date.strftime('%d-%m-%Y')
		temp['min_price'] = y[0]
		temp['max_price'] = y[1]
		temp['avg_price'] = y[2]
		final_p.append(temp)
		d = d +1
	d = 0
	for y in final_ans_g:
		date = presentday + timedelta(d)
		temp = {}
		temp['date'] = date.strftime('%d-%m-%Y')
		temp['min_price'] = y[0]
		temp['max_price'] = y[1]
		temp['avg_price'] = y[2]
		final_g.append(temp)
		d = d +1
	d = 0
	for y in final_ans_m:
		date = presentday + timedelta(d)
		temp = {}
		temp['date'] = date.strftime('%d-%m-%Y')
		temp['min_price'] = y[0]
		temp['max_price'] = y[1]
		temp['avg_price'] = y[2]
		final_m.append(temp)
		d = d +1
	response['onion'] = final_r
	response['potato'] = final_p
	response['garlic'] = final_g
	response['methi'] = final_m


	return JsonResponse(response)
