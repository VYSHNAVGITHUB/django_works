from django.shortcuts import render

from django.views.generic import View


from django import forms


# ===========================================================================================
from geopy.geocoders import Nominatim
 
def get_address(place):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(place)
    return getLoc.address

class GeoForm(forms.Form):
    place=forms.CharField()

class GeoView(View):
    def get(self,request,*args,**kwargs):
        form=GeoForm()
        return render(request,"geo.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=GeoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            place=form.cleaned_data.get("place")
            address=get_address(place)
            print(address)
        return render(request,"geo.html",{"form":form,"result":address})        









class OperationForm(forms.Form):
    num1=forms.IntegerField()
    num2=forms.IntegerField()




class ExponentView(View):
    def get(self,request,*args,**kw):
        form=OperationForm()
        return render(request,"exponent.html",{"form":form})
     
    
    def post(self,request,*args,**kw):
        form=OperationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")   
            result=n1**n2
        return render(request,"exponent.html",{"result":result,"form":form})    
    



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class LoginView(View):
    def get(self,request,*args,**kw):
        form=LoginForm()
        return render(request,"login.html",{"form":form}) 

class RegistrationForm(forms.Form):
    firstname=forms.CharField()
    lastname=forms.CharField()
    email=forms.EmailField()
    username=forms.CharField()
    password=forms.CharField()

class RegistrationView(View):
    def get(self,request,*args,**kw):
        form=RegistrationForm()
        return render(request,"registration.html",{"form":form})   
    def post(self,request,*args,**kw):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            print("form invalid") 
        return render(request,"registration.html")                   







class AdditionView(View):
    def get(self,request,*args,**kw):
        return render(request,"addition.html")
    
    def post(self,request,*args,**kw):
        # request.POST
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1+n2
        print(res)
        return render(request,"addition.html",{"result":res})
    
class SubstrationView(View):
    def get(self,request,*args,**kw):
        return render(request,"substraction.html") 

    def post(self,request,*args,**kw):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1-n2  
        print(res)
        return render(request,"substraction.html",{"result":res})

class MultiplicationView(View):
    def get(self,request,*args,**kw):
        return render(request,"multiplication.html")  
    
    def post(self,request,*args,**kw):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1*n2  
        print(res)
        return render(request,"multiplication.html",{"result":res})


class DivisionView(View):
    def get(self,request,*args,**kw):
        return render(request,"division.html") 
    
    def post(self,request,*args,**kw):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1//n2  
        print(res)
        return render(request,"division.html",{"result":res})
    
class CubeView(View):
    def get(self,request,*args,**kw):
        return render(request,"cube.html") 

    def post(self,request,*args,**kw):
        n=int(request.POST.get("num"))
        res=n**3
        return render(request,"cube.html",{"result":res}) 


    
class FactorialView(View):
    def get(self,request,*arg,**kw):
        return render(request,"fact.html") 

    def post(self,request,*args,**kw):
        n=int(request.POST.get("num"))

        
        fact=1

        for i in range(1,(n+1)):
            fact=fact*i
        return render(request,"fact.html",{"result":fact})
    
class ArmstrongView(View):
    def get(self,request,*args,**kw):
        return render(request,"armstrong.html") 
    
    def post(self,request,*args,**kw):
        num=request.POST.get("num")

        original=int(num)
        sum=0
        l=len(num)
        for n in num:
            sum=sum+ int(n)**l
        result=sum==original
        return render(request,"armstrong.html",{"result":result})    


    # def post(self,request,*args,**kw):
    #     num=request.POST.get("num")
    #     l=len(num)
    #     sum=0
    #     num=int(num)
    #     original=num
    #     while(num !=0):
    #         digit=num % 10
    #         sum=sum+(digit**l)
    #         num=num // 10
    #     result=num==original
    #     return render(request,"armstrong.html",{"res":result})   
     

                
class PrimeView(View):
    def get(self,request,*args,**kw):
        return render(request,"prime.html")
    
    def post(self,request,*args,**kw):
        n=int(request.POST.get("num"))

        flag=0
        for i in range(2,n):
            if n%i==0:
                flag==1
                break
        result="num is not prime" if flag==1 else "num is prime"
        return render(request,"prime.html",{"result":result})  


class EvenNumbersView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"even.html")

    def post(self,request,*args,**kwargs):
        l1=int(request.POST.get("limit1"))
        l2=int(request.POST.get("limit2"))


        evens=[num for num in range(l1,l2) if num %2==0]

        # for num in range(l1,l2):
        #     if num%2==0:
        #         evens.append(num)
        return render(request,"even.html",{"result":evens})  


class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html") 






            #work 1
              
class HealthView(View):
    def get(self,request,*args,**kw):

        return render(request,"health.html")
    def post(self,request,*args,**kw):
        tummy_size=request.POST.get("tsize")
        buttock_size=request.POST.get("bsize")
        gender=request.POST.get("gender")
        bmi=int(tummy_size)/int(buttock_size)
        bmi=round(bmi,2)
        context={"gender":""}

        
        if gender == "male":
            if bmi <= .95 :
                context["gender"] = "male"
                context["risk"]= "low"
                context["shape"]= "pear"
            elif bmi >= .96 and bmi <=1 :
                context["gender"]= "male"
                context["risk"]="moderate"
                context["shape"]="avocado"
            elif bmi > 1:
                context["gender"]="male"
                context["risk"]="high"
                context["shape"]="apple" 
        else:

            if bmi <= .80 :
                context["gender"] = "female"
                context["risk"]= "low"
                context["shape"]= "pear"
            elif bmi >= .81 and bmi <=85 :
                context["gender"]= "female"
                context["risk"]="moderate"
                context["shape"]="avocado"
            elif bmi > .85:
                context["gender"]="female"
                context["risk"]="high"
                context["shape"]="apple" 

            
        return render(request,"health.html",{"result":context})
        

