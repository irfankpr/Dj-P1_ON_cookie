from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def valid(request):
    if request.COOKIES.get("UserName") and request.COOKIES.get("PASS"):
        name=request.COOKIES.get('UserName')
        return render(request, 'home.html',{'name':name})
    else:
        return render(request, 'index.html')


def setcookie(request):
    name = request.POST['name']
    passw = request.POST['pass']
    res=render(request, 'home.html',{'name':name})
    res.set_cookie('UserName', name) 
    res.set_cookie('PASS', passw)
    return res
    
def login(request):
    return setcookie(request)
