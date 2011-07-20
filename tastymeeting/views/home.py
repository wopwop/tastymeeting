# Create your views here.
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render_to_response, HttpResponse, RequestContext, redirect
from tastymeeting.models import Profile
from django.contrib.auth.models import User
from tastymeeting.forms import signupForm, loginForm

def home(request):
    return render_to_response("index.html", context_instance=RequestContext(request))
    
# Classic login
    
def login(request):
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            # authenticate user
            user = authenticate(username = request.POST['email'], password = request.POST['password'])
            if user is not None:
                auth_login(request, user)
                return redirect("/meals/paris/")
            else:
                message = "Votre email ou mot de passe de connexion n'est pas valide."
                return render_to_response("login.html", {"message":message}, context_instance=RequestContext(request))
        else:
            # show form errors
            return render_to_response("login.html",{"form":form}, context_instance=RequestContext(request))
    else:
        return render_to_response("login.html",context_instance=RequestContext(request))
    
# Classic signup
    
def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            # check if user exist and create new account
            try:
                user = User.objects.get(username = request.POST['email'])
            except User.DoesNotExist:
                # create new account and redirect it to meals page
                new_user = User(username = request.POST['email'], first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
                new_user.set_password(request.POST['password'])
                new_user.save()
                # create user profile
                new_user_profile = Profile(user = new_user)
                new_user_profile.save()
                return redirect("/meals/paris")
            else:
                # show message that user exist
                message = "Un compte avec cette adresse email existe déjà."
                return render_to_response("signup.html", {"message":message}, context_instance=RequestContext(request))
        else:
            # form is invalide show errors
            return render_to_response("signup.html",{"form":form}, context_instance=RequestContext(request))
    else:
        return render_to_response("signup.html", context_instance=RequestContext(request))
    

# Manage login or signup with facebook
    
def fbconnect(request):
    if request.facebook:
        # Check if user exist
        facebook_user = request.facebook.graph.get_object("me")
        try:
            user = Profile.objects.get(username = facebook_user['email'])
        except Profile.DoesNotExist:
            
            # create new user and login it
            
            new_user = User(
                username = facebook_user['email'],
                first_name = facebook_user['first_name'],
                last_name = facebook_user['last_name'],
                email = facebook_user['email']
                )
            new_user.set_password(facebook_user['id'])
            new_user.save()
            
            # create a profile to the new user
            
            if(facebook_user['gender'] == "male"):
                new_user_sexe = "H"
            else:
                new_user_sexe = "F"
            
            new_user_profile = Profile(user = new_user, facebook = facebook_user['id'], sexe = new_user_sexe)
            new_user_profile.save()
            
            # login user to create session and redirect to meals page
            
            return HttpResponse("create done!")
        else:
            
            # login user to create session and redirect to meals page
            
            return HttpResponse("user exist!")

# Logout
def logout(request):
    auth_logout(request)
    return redirect("/")