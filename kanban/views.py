from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Board, SubCard, Cards
from .serializers import BoardSerializer, CardSerializer, SubCardSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_user']

class CardViewSet(ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

class SubCardViewSet(ModelViewSet):
    queryset = SubCard.objects.all()
    serializer_class = SubCardSerializer
    permission_classes = [IsAuthenticated]
    
        # sobreescribo para crear o actualizar un registro segun el id_user
    def create(self, request, *args, **kwargs):
        # si te entrega un id es porque si existe
        id = request.data.get('id')
        if id is not None:
            return super(SubCardViewSet, self).create(request, *args, **kwargs)
        
        subtask = SubCard.objects.filter(id=id).first()
        if subtask:
            serializer = self.get_serializer(subtask, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return super(SubCardViewSet, self).create(request, *args, **kwargs)
        