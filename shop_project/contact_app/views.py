from django.shortcuts import render,redirect
from contact_app.models import Contact
from contact_app.form import ContactForm

def success(request):
	return render(request,'success.html')

def contactform(request):
	
	if request.method =='POST':
		
		subject = request.POST.get('subject')
		email = request.POST.get('email')
		text = request.POST.get('text')
		
		Contact.objects.get_or_create(subject=subject,email=email,text=text)
		
		return redirect('contactform/success')

	contact = ContactForm()	
	return render(request,'formcontact.html',context={'contact':contact})

