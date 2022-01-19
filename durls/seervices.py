"""
This module is used for interacting with models. 

Ideally, only this module should import Model classes.

This module should contain function which accepts queryset parameter and returns a queryset.
"""
from durls.models import Destination


def destination_all():
    """
    Returns a queryset of all destinations.
    """
    return Destination.objects.all()


def destination_for_user(owner):
    """
    Returns a queryset of destinations for a user.
    """
    return Destination.objects.filter(owner=owner)
