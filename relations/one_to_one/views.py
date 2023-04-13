from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant


def index(req):
    pass


def create(req):
    place = Place(name='Place 1', address='Street 1')
    place.save()

    restaurant = Restaurant(place=place, number_of_employees=5)
    restaurant.save()

    return HttpResponse(restaurant.place.name)
