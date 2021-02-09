## view

from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def ProfileViewSet(request):
    all_profiles = Profile.objects.all()
    data = ProfileSerializer(all_profiles , many=True).data
    return Response({'data':data})
