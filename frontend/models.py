from django.db import models
from datetime import datetime
# Create your models here.
#creating the Gallery model for input and output images
class Gallery(models.Model):
	Date = models.DateTimeField(default=datetime.now, blank=True)
	Input_image=models.ImageField()
	Output_image=models.ImageField()

#creating Team model for saving the information about team members
class Team(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	roll_no = models.CharField(max_length=10)
	image = models.ImageField( upload_to="assets/images")
	facebook_url = models.URLField(max_length=200,default='SOME STRING')
	github_url = models.URLField(max_length=200,default='SOME STRING')
	linkedin_url = models.URLField(max_length=200,default='SOME STRING')




class AboutUs(models.Model):
	a_image = models.ImageField( upload_to="assets/images")
	description = models.CharField(max_length=500)


class Intro(models.Model):
	topic = models.CharField(max_length=100)
	i_image = models.ImageField(upload_to="assets/images")
	description = models.CharField(max_length=500)

    

	



    	
