from django.urls import path
from .views import PdfConvertor

app_name = 'convertor'

urlpatterns = [
    path('docx-to-pdf/', PdfConvertor.as_view())
]
