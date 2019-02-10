from api.models import MovementHistory
from api.serializers import MovementHistorySerializer
import requests
from workers import task


@task(schedule=10)
def send_request():
   request = requests.get('https://queue')
   if(request.status_code == 200):
      serializer = MovementHistorySerializer(MovementHistory.objects.all(), many=True)
      requests.put('https://queue', data=serializer.data)

