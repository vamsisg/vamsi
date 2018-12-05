from django.shortcuts import render
def user(request):
    return render(request,"login.html")
def log(request):
    user = request.POST.get("user")
    upass = request.POST.get("pass")
    res = request.POST.get("radio")
    d = ["naveen","vamsi","tripura"]
    c = ["123", "456", "23456"]
    a = ["admin", "user", "employee"]
    pos = d.index(user)
    if d[pos]== user and  c[pos] == upass:
        if a[pos] == res:
            mess = res
            return render(request,"login1.html",{"mess":mess})
        else:
            mess="it is not",res
            return render(request, "login1.html", {"mess": mess})
    else:
        mess = "invalid user name and password"
        return render(request, "login1.html", {"mess": mess})




