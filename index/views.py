from django.shortcuts import render
from django.http import HttpResponse, request
from .models import PopularDestination, PopularPlace, RecentTrip, Question
from django.shortcuts import get_list_or_404, get_object_or_404 
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import Contactform





def myindex(request):
	qs = PopularDestination.objects.all()
	ap = PopularPlace.objects.all()
	fe = RecentTrip.objects.all()
	contex = {'data':qs,'news':ap,'tea':fe}	
	return render(request, 'index/index.html',contex)

def mydetails(request, myid):
	a = get_object_or_404(PopularDestination, id=myid)
	# if request.method == "POST":
	# 	name = request.POST.get('name')
	# 	email = request.POST.get('email')
	# 	phone = request.POST.get('phone')
	# 	message = request.POST.get('message')
	# 	if form.is_valid():
	# 		form.save()

	# 	elif len(phone) != 11:
	# 		messages.error(request, 'Invalid phone')
	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			form.save()
		

	form = Contactform()



	context = {'data':a}
	return render(request, 'details/details.html', context)


def myabout(request, myid):
	a = get_object_or_404(PopularPlace, id=myid)


	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			form.save()
		

	form = Contactform()

	context = {'news':a}
	return render(request, 'about/look.html', context)



def contact(request):

	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject'] + "" + name
		message = request.POST['message']


		try:
			send_mail(
				subject,
				message,
				email,
				['thelighttravelsandtour@gmail.com'],
				fail_silently=False,
				)
		except BadHeaderError:
			return HttpResponse('invalid header found')
		return render(request, 'contact/contact.html', {'name':subject})
	return render(request, 'contact/contact.html')