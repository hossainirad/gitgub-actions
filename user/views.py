from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from user.tasks import check_celery
from django.core.cache import cache


class CheckCelery(APIView):
	permission_classes = []
	authentication_classes = []
	def get(self, request):
		print('the key set!')
		check_celery.apply_async()
		return Response("celery checked!")
