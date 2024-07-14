from django.urls import path
from .views import GenerateRegexAPI

urlpatterns = [
    path('generate-regex', GenerateRegexAPI.as_view(), name='generate-regex'),
]
