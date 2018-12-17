from django.shortcuts import render
from shop_app.models import Product,Client,Comment
from shop_app.forms import CommentForm
import datetime


def index(request):
  products = Product.objects.all()
  return render(request, 'index.html', context={ 'products': products })


def product(request, product_id):
	product = Product.objects.get(id=product_id)
	comments = Comment.objects.all().filter(product_id=product.id)
	return render(request,'product.html',context={'product': product,"comments":comments})

def clients(request):
	clients=Client.objects.all()
	return render(request,'clients.html',context={'clients':clients})

def client(request,client_id):
	client = Client.objects.get(id=client_id)
	return render(request,'client.html',context={'client':client})

def form(request,product_id):
	
	if request.method =='POST':
		
		username = request.POST.get('username')
		
		text = request.POST.get('text')
		
		product=Product.objects.get(id=product_id)
		
		date=datetime.datetime.now()
		
		Comment.objects.get_or_create(username=username,text=text,date=date,product=product)
	
	form = CommentForm()	
	
	return render(request,'forms.html',context={'form':form})


