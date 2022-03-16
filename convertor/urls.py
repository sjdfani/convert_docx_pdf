from django.urls import path
from .views import PdfConvertor

app_name = 'convertor'

urlpatterns = [
    path('test/', PdfConvertor.as_view())
]
