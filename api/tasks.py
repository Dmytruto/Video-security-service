
from api.views import MovementHistoryListCreate, namesListCreate
from api.models import MovementHistory

from workers import task

@task(schedule=10)
def send_request():
    MovementHistory.objects.create()