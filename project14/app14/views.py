from django.shortcuts import render
def showIndex(request):
    return render(request,"index.html")
def showDetails(request):
    str = request.POST.get("radio")
    return render(request,"index.html",{"message": str})
