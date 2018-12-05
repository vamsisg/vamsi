from django.shortcuts import render
def indexFile(request):
    return render(request,"index.html")
def showDetails(request):
    name  = request.POST.get("t1")
    desig = request.POST.get("t4")
    phone = request.POST.get("t2")
    idno  = request.POST.get("t3")
    firstname = request.POST.get("t5")
    d1={
        "name":name,
        "phone":phone,
        "idno":idno,
        "desig":desig,
        "firstname":firstname
    }
    return render(request,"details.html",d1)
