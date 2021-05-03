from celery import Celery
from . import tasks  # noqa

app = Celery("api")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("app.settings:settings", namespace="CELERY")

# Load task modules
app.autodiscover_tasks()
