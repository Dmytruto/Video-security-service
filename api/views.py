from api.models import MovementHistory
from api.serializers import MovementHistorySerializer
from rest_framework import generics




class MovementHistoryListCreate(generics.ListCreateAPIView):
    queryset = MovementHistory.objects.all()
    serializer_class = MovementHistorySerializer
