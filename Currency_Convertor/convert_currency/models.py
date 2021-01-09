from django.db import models

class Currency(models.Model):
	currency = models.CharField(max_length = 20)
	shortform = models.CharField(max_length =6,default="", editable=True)

	def __str__(self):
		return self.currency

	class Meta:
		verbose_name_plural = 'Currencies'

#History of all the conversions did
class History(models.Model):
	To = models.CharField(max_length =20,default ="INR",blank = True)
	From = models.CharField(max_length =20 ,default = "USD",blank=True)
	Amount = models.FloatField(blank = True,default = 1.0,) 
	Result = models.FloatField(blank =True,null =True) 
	Conversion_factor = models.FloatField(blank = True,null=True) 

	Date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.Result

class Feedback(models.Model):
	name = models.CharField(max_length = 50)
	subject= models.CharField(max_length = 60)
	comment = models.CharField(max_length = 300)

	def __str__(self):
		return self.subject




