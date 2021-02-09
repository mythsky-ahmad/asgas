from django.urls import path
from .views import my_profile_views
from . import api

app_name ='profiles'

urlpatterns = [
    path('myprofile/' , my_profile_views , name= 'my_profile_views'),



    # api

    path('api/list/' , api.ProfileViewSet , name= 'profileList'),
]