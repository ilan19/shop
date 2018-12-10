import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')
import django
django.setup()
import random
from faker import Faker
from shop_app.models import Client,Product

# CONSIGNE
# creez 2 fonctions :
#   1. cree 1000 faux clients
#   2. cree 50 faux produits
Fakegen = Faker()
def generate_brand():
	brands=["Nike","Adidas","Jordan","balanciaga","Rebook","Timberland", "Scholl","Asics","Tatan","Geox"]
	index=random.randint(0,9)
	return brands[index]



def create_clients():
	for client in range(0,1000):
		client = Client.objects.get_or_create(first_name=Fakegen.first_name(),last_name=Fakegen.last_name(),password=Fakegen.password(),email=Fakegen.email())[0]
		print(client)

def generate_products():
	for product in range(50):
		price=random.randint(30,150)
		brand=generate_brand()
		product = Product.objects.get_or_create(name=brand,price=price,description=Fakegen.text(max_nb_chars=400))[0]
		print(product)
		
 

 
def populate():
	#create_clients()
	generate_products()

if __name__ == '__main__':
  print('starting populate...')
  populate()
  print('done populating')