from django.urls import path
from .views import ListCreateUserAPIView, RetrieveUpdateUserAPIView

urlpatterns = [
    path("", ListCreateUserAPIView.as_view()),
    path("<int:pk>/", RetrieveUpdateUserAPIView.as_view())
]
