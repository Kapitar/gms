from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer


class ListCreateUserAPIView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    

class RetrieveUpdateUserAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = "pk"