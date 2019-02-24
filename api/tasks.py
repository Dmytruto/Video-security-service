from api.models import MovementHistory
from api.serializers import MovementHistorySerializer
import requests
from workers import task


@task(schedule=1)
def send_request():
   request = requests.get('http://127.0.0.1:8000/ideal/')
   if(request.status_code == 200):
      serializer = MovementHistorySerializer(MovementHistory.objects.all(), many=True)
      requests.put('http://127.0.0.1:8000/idealpost/', data=serializer.data)

