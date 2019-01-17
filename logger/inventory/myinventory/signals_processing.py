from django.shortcuts import render
from django.dispatch import receiver
from crequest.middleware import CrequestMiddleware
from .models import Items
from .signals import state_audit_signal


@receiver(state_audit_signal)
def user_change_status_signal(sender,**kwargs):
    current_request=CrequestMiddleware.get_request()
    user_id=kwargs['user']
    change=kwargs['change']
    print("recieved signal")
