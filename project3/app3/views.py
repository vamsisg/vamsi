from django.shortcuts import render
def showIndex(request)
    merchant = {
               "admin":{
                    "username":"admin",
                    "password":"vamsi"
               }
               "stocks":
                   {
                       "101":{"name":"vamsi","salary":10000},
                       "101":{"name":"vamsi","salary":10000},
                       "101":{"name":"vamsi","salary":10000},

                   }
    }
     return render(request,"index.html" {"emp":merchant})