from rest_framework import serializers , viewsets , routers

from .models import Profile 

class ProfileSerializer(serializers.ModelSerializer):#HyperlinkedModelSerializer
    class Meta:
        model = Profile
        fields = '__all__'