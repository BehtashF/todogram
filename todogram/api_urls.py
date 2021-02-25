from rest_framework import routers
from todoapi.views import TaskViewset


router = routers.SimpleRouter()
router.register('task', TaskViewset, basename='task')