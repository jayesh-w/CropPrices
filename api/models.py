from django.db import models

# Create your models here.
#model 1 daily price model
#model 2 only price of 10 crops 


class DailyPrice(models.Model):
	name = models.CharField(max_length=100,default="NULL")
	measure = models.CharField(max_length=100,default="NULL")
	arrival = models.CharField(max_length=100,default="NULL")
	commodity = models.CharField(max_length=100,default="NULL")
	min_price = models.IntegerField(default=0)
	max_price = models.IntegerField(default=0)
	avg_price = models.IntegerField(default=0)


class SelectedPrice(models.Model):
	name = models.CharField(max_length=100, default="NULL")
	measure = models.CharField(max_length=100, default="NULL")
	arrival = models.CharField(max_length=100, default="NULL")
	date = models.DateField(max_length=100, default="NULL")
	min_price = models.IntegerField(default=0)
	max_price = models.IntegerField(default=0)
	avg_price = models.IntegerField(default=0)

class DailyPriceLog(models.Model):
	date = models.CharField(max_length=100, default="NULL")
	result = models.CharField(max_length=100, default="NULL")



