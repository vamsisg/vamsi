from django.shortcuts import render
def show(request):
    return render(request,"index1.html")
def details(request):
    res = request.POST.getlist("cheech")
    return render(request,"index2.html" ,{"message":res})
