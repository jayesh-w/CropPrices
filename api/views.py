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
import datetime
import tabula
from api.models import DailyPrice,DailyPriceLog
# Create your views here.


def index(request):
	return HttpResponse("Hello Farmos")

def dailyprice(request):
	#fetch the code from sqlite3 database
	#add the data to the list
	#append the list to a dictionary
	#return the dictionary

	result = [] #result list 
	daily_price_dict = {'name':'Onion','measure':'Quintal','min_price':10,'max_price':12,'avg_price':11,'commodity_number':4062}
	result.append(daily_price_dict)
	# final_result = {'date':'18 December 2021','size':1,'result':result}
	


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
	x = datetime.datetime.now()
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

	return JsonResponse({'result':'success'})






