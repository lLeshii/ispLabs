import time

from lab3_django.celery import app
from cart.models import Order
import time


@app.task
def deliver(id):
    ords = Order.objects.get(id=id)
    ords.status = "received"
    ords.save()


@app.task
def deliver_group(ord_list):
    for ords in ord_list:
        deliver.delay(ords)