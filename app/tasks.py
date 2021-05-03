from celery import shared_task
import time


@shared_task
def add(x, y):
    # simulates long lasting task
    time.sleep(30)
    return x + y
