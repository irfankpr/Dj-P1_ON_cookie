from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def valid(request):
    if request.COOKIES.get("UserName") and request.COOKIES.get("PASS"):
        Cname=request.COOKIES.get('UserName')
        Cpassw=request.COOKIES.get('PASS')
        Sname=request.session['UserName']
        Spassw=request.session['PASS']

        if Cname==Sname and Cpassw==Spassw:
            return render(request, 'home.html',{'name':Cname})
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def setcookie(request):
    name = request.POST['name']
    passw = request.POST['pass']
    request.session['UserName'] = name
    request.session['PASS'] = passw
    res=render(request, 'home.html',{'name':name})
    res.set_cookie('UserName', name) 
    res.set_cookie('PASS', passw)
    return res
    
def login(request):
    name = request.POST['name']
    passw = request.POST['pass']
    if name=='rakeeb' and passw=='dana123':
        return setcookie(request)
    else:
        return render(request, 'index.html',{'err':"invalid credinals"})

def Sout(request):
    res=render(request, 'index.html')
    res.delete_cookie('UserName')
    res.delete_cookie('PASS')
    del request.session['UserName']
    del request.session['PASS']
    return res