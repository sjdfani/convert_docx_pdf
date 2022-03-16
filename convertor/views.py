from docx2pdf import convert
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.core.files.storage import default_storage


class PdfConvertor(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        file_obj = request.data['file']
        file_name = default_storage.save(file_obj.name, file_obj)
        file = default_storage.open(file_name, 'rb')
        convert(str(file), f"{file.name}.pdf")
        new_file = default_storage.url(f"{file.name}.pdf")
        message = {
            "link": new_file
        }
        return Response(message, status=status.HTTP_200_OK)
