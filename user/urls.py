from django.urls import path
from user.views import *

app_name = 'user'

urlpatterns = [
	path('check-celery/', CheckCelery.as_view(), name='check_celery'),
]
