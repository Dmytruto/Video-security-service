from api.models import MovementHistory, Names
from api.serializers import MovementHistorySerializer, NamesSerializer
from rest_framework import generics


class namesListCreate(generics.ListCreateAPIView):
    queryset = Names.objects.all()
    serializer_class = NamesSerializer

class MovementHistoryListCreate(generics.ListCreateAPIView):
    queryset = MovementHistory.objects.all()
    serializer_class = MovementHistorySerializer
