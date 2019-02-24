from api.models import MovementHistory
from api.serializers import MovementHistorySerializer
import requests
from workers import task
import time
import cv2
import numpy as np



@task(schedule=1)
def send_request():
   print(2)
   pass
#    request = requests.get('http://127.0.0.1:8000/ideal/')
#    if(request.status_code == 200):
#       serializer = MovementHistorySerializer(MovementHistory.objects.all(), many=True)
#       requests.put('http://127.0.0.1:8000/idealpost/', data=serializer.data)


@task(schedule=100)
def perform_video_stream():
   start = time.time()
   cap = cv2.VideoCapture(0)
   while True:
      ret, frame = cap.read()
      cv2.imshow("frame", frame)
      end = time.time()
      if int(end - start) > 10 or cv2.waitKey(1) == 13 :
         break

   cap.release()
   cv2.destroyAllWindows()




