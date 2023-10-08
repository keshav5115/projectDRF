from django.urls import path
from userapp.api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('register/',views.RegisterVW,name='register'),
    path('login/',obtain_auth_token,name='login'),
    path('logout/',views.LogoutVW,name='logout'),
]