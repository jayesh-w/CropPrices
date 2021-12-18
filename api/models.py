from django.db import models

# Create your models here.
#model 1 daily price model
#model 2 only price of 10 crops 


class DailyPrice(models.Model):
	name = models.CharField(max_length=100)
	measure = models.CharField(max_length=100)
	arrival = models.CharField(max_length=100)
	commodity = models.CharField(max_length=100)
	min_price = models.IntegerField()
	max_price = models.IntegerField()
	avg_price = models.IntegerField()


class SelectedPrice(models.Model):
	name = models.CharField(max_length=100)
	measure = models.CharField(max_length=100)
	arrival = models.CharField(max_length=100)
	date = models.DateField(max_length=100)
	min_price = models.IntegerField()
	max_price = models.IntegerField()
	avg_price = models.IntegerField()



