from django.shortcuts import render
def index(request):
    a1={
        "idno":1024,
        "name":"vamsi",
        "desig":"teammember"
    }
    return render(request,"index.html",a1)
