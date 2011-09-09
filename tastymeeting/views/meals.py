# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, HttpResponse, redirect, RequestContext, get_list_or_404
from django.contrib.auth.models import User
from tastymeeting.models import Repas, Profile, Reservation


def meals(request, location='Paris'):
    meals = get_list_or_404(Repas, restaurant__ville__nom=location)
    people = Profile.objects.filter(ville = location)
    new_meals = []
    for meal in meals:
        reservations = meal.reservation_set.all()[:4]
        meal.reservations = reservations
        meal.places_rest = meal.places - meal.reservation_set.count()
        new_meals.append(meal)
    return render_to_response("meals.html", {"meals":meals, "people":people},context_instance = RequestContext(request))
    
def meal_details(request, restaurant, meal_id):
    return HttpResponse(restaurant)
