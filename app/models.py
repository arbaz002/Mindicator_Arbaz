from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=200,null=False)
	email = models.EmailField(null=True)
	location = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.user.username

class Agent(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField(max_length=200,null=False)
	email = models.EmailField(null=True)

	def __str__(self):
		return self.user.username

class Station(models.Model):
	name = models.CharField(max_length=200,primary_key=True)

	def __str__(self):
		return self.name

class Train(models.Model):
	arrival_station = models.ForeignKey(Station,on_delete=models.CASCADE,related_name="arrival_train")
	destination_station = models.ForeignKey(Station,on_delete=models.CASCADE,related_name="destination_train")
	arrival_time = models.TimeField()
	destination_time = models.TimeField()

	def __str__(self):
		train_id="T"+"0"*(6-len(str(self.id)))+str(self.id)
		return train_id



