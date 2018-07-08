from rest_framework import serializers
from fileuploadapp.models import UploadMedia
class UploadMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadMedia
        fields = ('id', 'file_name', 'uploaded_at')
