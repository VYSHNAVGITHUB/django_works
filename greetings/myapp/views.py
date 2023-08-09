from django.shortcuts import render

from django.views.generic import View

class GoodMorningView(View):
    def get(self,request,*args,**kw):
        return render(request,"morning.html")
    

class GoodAfternoonView(View):
    def get(self,request,*args,**kw):
        return render(request,"afternoon.html")
    
class GoodEveningView(View):
    def get(self,request,*args,**kw):
        return render(request,"evening.html")