from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from.models import product
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
class InsertView(View):
    def post(self,request):
        p_id=int(request.POST['t1'])
        p_name=request.POST['t2']
        p_cost=float(request.POST['t3'])
        p_mfdt=request.POST['t4']
        p_expdt=request.POST['t5']
        p1=product(pid=p_id, pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        resp=HttpResponse("product inserted successfullly")
        return resp
class InsertInput(View):
    def get(self,request):
        return render(request,'productinput.html')
class DisplayView(View):
    def get(self,request):
        qs=product.objects.all()
        con_dic={"records":qs}
        return render(request,"display.html",con_dic)

class DeleteInputView(View):
    def get(self,request):
        return render(request,'deleteinput.html')
class UpdateInputView(View):
    def get(self,request):
        return render(request,'updateinput.html')

class UpdateView(View):
    def post(self,request):
        p_id=int(request.POST["t1"])
        p_name=request.POST["t2"]
        p_cost=float(request.POST["t3"])
        p_mfdt=request.POST["t4"]
        p_expdt=request.POST["t5"]
        prod=product.objects.get(pid=p_id)
        prod.pname=p_name
        prod.pcost=p_cost
        prod.pmfdt=p_mfdt
        prod.pexpdt=p_expdt
        prod.save()
        resp=HttpResponse("product update successfully")
        return resp

class DeleteView(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        prod=product.objects.filter(pid=p_id)
        prod.delete()
        resp=HttpResponse("product deleted successfully")
        return resp






















