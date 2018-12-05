from django.shortcuts import render
def index(request):
    d1 = {
        "101": {"name": "vams", "salary": 190000},
        "103": {"name": "vams", "salary": 190},
        "106": {"name": "vams", "salary": 40000},
        "109": {"name": "vams", "salary": 10000},
    }
    return render(request , "index.html" , {"emp": d1})
