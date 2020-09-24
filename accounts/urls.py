from django.urls import path,include


from . import views
from . import api_view

app_name = 'accounts'
urlpatterns = [
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('register/', views.user_register, name='register'),
	path('api/register',api_view.CreateUserAPIView.as_view(),name= 'api-register' ),
	path('api/activate',api_view.Activate.as_view(),name= 'api-activate' )
]