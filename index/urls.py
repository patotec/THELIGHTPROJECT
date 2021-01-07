from django.urls import path
from . import views

app_name = 'indexurl'
urlpatterns = [
	path('', views.myindex, name='index'),
	path('details/<slug:myid>',  views.mydetails ,name="details" ),
	path('about/<slug:myid>',  views.myabout ,name="look" ),
	path('contact', views.contact, name="contact" ),



    ]
