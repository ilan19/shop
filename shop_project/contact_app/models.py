from django.db import models

class Contact(models.Model):
	subject=models.CharField(max_length=100)
	email=models.EmailField()
	text=models.TextField(max_length=264)

	def __str__(self):
		return self.email

	def __repr__(self):
		return "<Contact {}>".format(self.email)
	
		
