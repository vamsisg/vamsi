from django.shortcuts import render
def index(request):
    return render(request,"login.html")
def validate(request):
    uname =request.POST.get("name")
    upass = request.POST.get("pass")
    if (uname =="sathya" and upass == "tech")or (uname =="vamsi" and upass == "1234")or(uname =="naven" and upass == "5672"):
        message = "welcome"+uname
        return render(request,"welcome.html",{"message":message})
    else:
        message = "invalid"
        return render(request,"login.html",{"message":message})




