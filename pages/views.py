from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user) 
    print(args,kwargs)
    print(request)
    #return HttpResponse("<h1>Hello Dad and Mom and Jennie and Susie!!</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "some fun words",
        "my_number": 7800,
        "my_list": [305, 1812, 999]
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})