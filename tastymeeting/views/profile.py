# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, HttpResponse, redirect, RequestContext
from django.contrib.auth.models import User
from tastymeeting.models import Profile
from tastymeeting.forms import profileForm

def settings_profile(request):
    if request.method == "POST":
        form = profileForm(request.POST, request.FILES, instance=request.user.get_profile())
        if form.is_valid():
            form.user = request.user
            updated_profile = form.save()
            success = "ok"
            message = "Vos paramètres ont bien été enregistré"
            return render_to_response("settings.html", {"success":success, "message":message}, context_instance=RequestContext(request))
        else:
            return render_to_response("settings.html", {"form":form}, context_instance=RequestContext(request))
    else:    
        return render_to_response("settings.html", context_instance=RequestContext(request))