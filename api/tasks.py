from api.models import MovementHistory
from api.serializers import MovementHistorySerializer
import requests
from workers import task
import time
import cv2
import numpy as np


cap = cv2.VideoCapture(0)


@task(schedule=1)
def send_request():
   print(2)
   pass
#    request = requests.get('http://127.0.0.1:8000/ideal/')
#    if(request.status_code == 200):
#       serializer = MovementHistorySerializer(MovementHistory.objects.all(), many=True)
#       requests.put('http://127.0.0.1:8000/idealpost/', data=serializer.data)


@task(schedule=20)
def perform_video_stream():
   start = time.time()
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter('video/' + str(start) + '.avi', fourcc, 20.0, (640, 480))
   while True:
      ret, frame = cap.read()
      frame = cv2.flip(frame, 0)
      out.write(frame)
      cv2.imshow("frame", frame)
      end = time.time()
      dif = int(end - start)
      print(dif)
      if dif > 10 or cv2.waitKey(1) == 13 :
         break
   cv2.destroyAllWindows()




