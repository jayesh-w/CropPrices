#ChangeLog
#Version 1.0.0 -- Jayesh
#	--- Adding Basic Functions for the API's

# path('/dailyprice',views.dailyprice,name='index'),
# 	path('/activateprice',views.activateprice),
# 	path('/crop-price',views.cropprice), 


from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
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
	final_result = {'date':'18 December 2021','size':1,'result':result}

	return JsonResponse(final_result)

def activateprice(request):
	#check the user credentials
	#fire the wget function 
	#check if the file is stored with price-date.pdf
	#start tabula.py
	#truncate the current-daily-price table
	#add the new values to the table
	#return finish

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






