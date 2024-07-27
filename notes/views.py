from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Notes
from .serializers import NotesSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class NotesViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']
