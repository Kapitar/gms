from django.urls import path
from .views import ListGradeAPIView, CreateGradeAPIView, DestroyGradeAPIView, RetrieveGradeAPIView

urlpatterns = [
    path("grades/<int:student_id>/", ListGradeAPIView.as_view()),
    path("grades/create/", CreateGradeAPIView.as_view()),
    path("grades/delete/<int:pk>/", DestroyGradeAPIView.as_view()),
    path("grades/<int:student_id>/assignment/<int:assignment_id>", RetrieveGradeAPIView.as_view()),
]