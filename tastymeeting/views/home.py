# Create your views here.

from django.shortcuts import render_to_response, HttpResponse

def home(request):
    return render_to_response("index.html")
    
def loginbox(request):
    return render_to_response("loginbox.html")
    
def signup(request):
    return HttpResponse("test")