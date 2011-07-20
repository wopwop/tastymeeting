# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, HttpResponse, redirect, RequestContext
from django.contrib.auth.models import User
from tastymeeting.models import Repas, Profile


def meals(request, location='Paris'):
    return render_to_response("meals.html", context_instance=RequestContext(request))
    
