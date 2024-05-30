from django.shortcuts import render,redirect,HttpResponse
from empapp.models import employee_model
# Create your views here.
def index(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        addr=request.POST['addr']
        context={}
        if fname=='' or lname=='' or age=='' or addr=='':
            context['msg']="Fields cannot be empty"
        else:
            c=employee_model.objects.create(fname=fname,lname=lname,age=age,address=addr)
            c.save()
            context['msg']="Employee Added"
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')

def display(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        addr=request.POST['addr']
        context={}
        if fname=='' or lname=='' or age=='' or addr=='':
            context['msg']="Fields cannot be empty"
        else:
            c=employee_model.objects.create(fname=fname,lname=lname,age=age,address=addr)
            c.save()
            context['msg']="Employee Added"
        d=employee_model.objects.all()
        
        context['data']=d
        return render(request,'index.html',context)
    else:
        c=employee_model.objects.all()
        context={}
        context['data']=c
        return render(request,'index.html',context)

def search(request):
    cat=request.POST['category']
    opt=request.POST['options']
    string=request.POST['search_string']
    if len(string) == 0:
        string="error"
    context={}
    url="empapp/"+cat+"/"+opt+"/"+string
    print(url)
    return redirect(url)

def look(request,cid,oid,txt):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        addr=request.POST['addr']
        context={}
        if fname=='' or lname=='' or age=='' or addr=='':
            context['msg']="Fields cannot be empty"
        else:
            c=employee_model.objects.create(fname=fname,lname=lname,age=age,address=addr)
            c.save()
            context['msg']="Employee Added"
        d=employee_model.objects.all()
        
        context['data']=d
        return render(request,'index.html',context)
    else:
        context={}
        if cid== "empname":
            c=employee_model.objects.all()
            context['data']=[]
            if oid== "startswith":
                for x in c:
                    if x.fname.lower() == txt.lower():
                        context['data'].append(x)
                if len(context['data']) == 0:
                    context['errmsg']="No Data found"
            elif oid== "contains":
                for x in c:
                    if x.fname.lower() == txt.lower() or x.lname.lower() == txt.lower():
                        context['data'].append(x)
                if len(context['data']) == 0:
                    context['errmsg']="No Data found"
            else:
                context['error']="Invalid lookup option! Please choose starts with or contains option"


        else:
            if oid== "lte":
                ag=int(txt)
                c=employee_model.objects.filter(age__lte=ag)
                context['data']=c
                if len(context['data']) == 0:
                    context['errmsg']="No Data found"
            else:
                context['error']="Invalid lookup option! Please choose age less than option"
        return render(request,'index.html',context)