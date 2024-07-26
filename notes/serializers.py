from .models import Notes
from rest_framework.serializers import ModelSerializer


class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
