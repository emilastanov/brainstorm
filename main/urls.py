from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('', GetSameWordsView.as_view()),
]