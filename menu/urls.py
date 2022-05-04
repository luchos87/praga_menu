from django.urls import path
from .views import MenuList, MenuDetailView

urlpatterns = [
    path('', MenuList.as_view()),
    path('<int:id>', MenuDetailView.as_view()),
]