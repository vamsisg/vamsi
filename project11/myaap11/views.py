from django.shortcuts import render
def fun1(request):
    return render(request,"login1.html")
def validation(request):
    uname =request.POST.get("name")
    upass = request.POST.get("pass")
    if (uname =="sathya" and upass == "tech")or:
        message = "welcome"
        return render(request,"welcome1.html",{"message":message})
    else:
        message = "invalid"
        return render(request,"login1.html",{"message":message})

