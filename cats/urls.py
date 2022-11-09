from django.urls import path
from .views import CatView


urlpatterns = [
    path("cats/", CatView.as_view()),
]
