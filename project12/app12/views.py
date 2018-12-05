from django.shortcuts import render
def index(request):
    return render(request,"check.html")
def validate(request):
    req = request.POST.getlist("lang")
    return render(request,"details.html",{"d1":req})



