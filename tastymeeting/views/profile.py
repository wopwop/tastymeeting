# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, HttpResponse, redirect, RequestContext
from django.contrib.auth.models import User
from tastymeeting.models import Profile
from tastymeeting.forms import profileForm, PasswordForm

def settings_profile(request):
    if request.method == "POST":
        form = profileForm(request.POST, request.FILES, instance=request.user.get_profile())
        if form.is_valid():
            form.user = request.user
            updated_profile = form.save()
            
            if "first_name" in request.POST:
                request.user.first_name = request.POST['first_name']
                request.user.save()
            if "last_name" in request.POST:
                request.user.last_name = request.POST['last_name']
                request.user.save()
            
            success = True
            message = "Vos paramètres ont bien été enregistré"
            return render_to_response("settings/settings.html", {"success":success, "message":message}, context_instance=RequestContext(request))
        else:
            return render_to_response("settings/settings.html", {"form":form}, context_instance=RequestContext(request))
    else:    
        return render_to_response("settings/settings.html", context_instance=RequestContext(request))
        
def settings_pass(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            # check if passwords are matching
            if request.POST['password'] == request.POST['repassword']:
                # update user password
                request.user.set_password(request.POST['password'])
                request.user.save()
                success = True
                message = "Votre mot de passe a été modifié avec succès"
                return render_to_response("settings/password.html", {"success":success, "message":message}, context_instance = RequestContext(request))
            else:
                error = "bla bla"
                return render_to_response("settings/password.html", {"error":error}, context_instance = RequestContext(request))
        else:
            return render_to_response("settings/password.html", {"form":form}, context_instance=RequestContext(request))
    else:
        return render_to_response("settings/password.html", context_instance=RequestContext(request))