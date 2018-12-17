from django.db import models

class Product(models.Model):
  name = models.CharField(max_length=264)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  description = models.TextField()
  image = models.ImageField(default='static/images/image.png', upload_to='static/images/')

  # def __str__(self):
  #   return self.description

  # def __repr__(self):
  #   return "<Product {}>".format(self.name)

class Client(models.Model):
	first_name = models.CharField(max_length=264)
	last_name = models.CharField(max_length=264)
	password = models.CharField(max_length=50)
	email = models.EmailField()
	profil_picture = models.ImageField(default="static/images/ecran.png", upload_to='static/images/')

	def __str__(self):
		return self.first_name

	def __repr__(self):
		return "<Client {}>".format(self.email)

class Comment(models.Model):
	username = models.CharField(max_length=264)
	text = models.TextField(max_length=500)
	date = models.DateField()
	product = models.ForeignKey(Product , on_delete=models.CASCADE)

	def __str__(self):
		return self.username

	def __repr__(self):
		return "<Comment {}>".format(self.username)