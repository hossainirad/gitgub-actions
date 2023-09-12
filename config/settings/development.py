from .base import *


load_dotenv('development.env', override=True)

DEBUG = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': os.environ.get('POSTGRES_HOST'),
#         'NAME': os.environ.get('POSTGRES_DB'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'PORT': os.environ.get('POSTGRES_PORT'),
#     }
# }

# # Redis
# REDIS_HOST = os.environ.get('REDIS_HOST')
# REDIS_USER = os.environ.get('REDIS_USER')
# REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
# REDIS_PORT = os.environ.get('REDIS_PORT')

# Cache settings
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': f'redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0',
#         'LOCATION': f'redis://127.0.0.1:6379/0',
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#             'PASSWORD': REDIS_PASSWORD,
#             'SOCKET_CONNECT_TIMEOUT': 4,  # seconds
#             'SOCKET_TIMEOUT': 4,  # seconds
#         },
#         'KEY_PREFIX': 'dockerized',
#     }
# }

# CELERY_RESULT_BACKEND = 'default'
CELERY_CACHE_BACKEND = 'default'

CELERY_BROKER_URL = f'redis://{REDIS_USER}:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/0'
# CELERY_BROKER_URL = f'redis://dockerized_redis:6379/0'

CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = "Asia/Tehran"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += ['rest_framework.renderers.BrowsableAPIRenderer']