from django.urls import path
from .views import EncuestaList, EncuestaDetailView

urlpatterns = [
    path('', EncuestaList.as_view()),
    path('<int:id>', EncuestaDetailView.as_view()),
]