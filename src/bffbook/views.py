from django.http import HttpResponse, response
from django.shortcuts import render

def home_view(request):
    user = request.user
    hello = "hellooo"
    context = {"user":user ,"hello":hello }
    return render(request, "main/home.html", context )
