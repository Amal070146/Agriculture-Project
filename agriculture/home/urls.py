from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from home import views

urlpatterns = [
	path("", views.home),
	path("login/",views.login),
	path("signup/",views.signup),

	#farmers
	path("farmers_table/",views.farmers_table),

	#retailers
	path("retailers_table/",views.retailers_table),

	#cold storage
	path("cold_storage/",views.cold_storage)


	]