from __future__ import absolute_import, unicode_literals
from celery import shared_task
import time


@shared_task
def check_celery():
	time.sleep(5)
	print('baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
	return 'naaaaaaaaaaaaaaaaaaaaaa'
