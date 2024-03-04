from django.shortcuts import render,HttpResponse, redirect
#from message_app.models import Msg
from .models import Msg
# Create your views here.

def testing(request):
    return HttpResponse("Linked successfully")

def create(request):
    print("Request is:",request.method)
    if request.method=='POST':
        #access form data
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mob']
        msg=request.POST['msg']
        #print(n,"-",mail,"-",mob,"-",msg)
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        return redirect('/dashboard')
        #return HttpResponse("Data Fetched")
    else:
        return render(request,'create.html')
    
def dashboard(request):
    m=Msg.objects.all()
    # print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)
    #return HttpResponse("Data fetched from database")

def delete(request,rid):
    #print("Id to be deleted:",rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')
    #return HttpResponse("id to be deleted:"+rid)

def edit(request,rid):
    #print("Id to be edited:",rid)
    if request.method=='POST':
        #update new data
        upname=request.POST['uname']
        upemail=request.POST['uemail']
        upmob=request.POST['mob']
        upmsg=request.POST['msg']
        m=Msg.objects.filter(id=rid)    #queryset
        m.update(name=upname,email=upemail,mobile=upmob,msg=upmsg)
        return redirect('/dashboard')
    else:
        #form with old data
        context={}
        m=Msg.objects.get(id=rid)  #msg object(2)
        #print(m)
        context['data']=m
        return render(request,'edit.html',context)
    #return HttpResponse("id to be edited:"+rid)
