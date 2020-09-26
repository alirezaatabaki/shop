from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('register/', views.user_register, name='register'),
	path('detail/', views.user_detail, name='detail'),
	path('add-address/', views.AddressCreate.as_view(), name='add-address')
]