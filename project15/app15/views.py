from django.shortcuts import render
def show(request):
    return render(request, "details.html")
def showDeta(request):
    str = request.POST.get("s1")
    return render(request, "details.html", {"message": str})
