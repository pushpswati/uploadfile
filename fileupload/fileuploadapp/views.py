from fileuploadapp.models import UploadMedia
from fileuploadapp.serializer import UploadMediaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser, MultiPartParser,JSONParser



class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        file_obj = request.data['file_name']

        UploadMedia.objects.create(file_name=file_obj)
        file_data_obj=UploadMedia.objects.all()
        serializer_data=UploadMediaSerializer(file_data_obj,many=True)
        return Response(serializer_data.data,status=status.HTTP_200_OK)
