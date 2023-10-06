from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Employee,Department

# Create your views here.
def home(request):
    emps=Employee.objects.all()

    return render(request,"employee/home.html",{
        'emps':emps
    })

def addEmp(request):
    if request.method=="POST":
        print('data is coming')

        # data fetch
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=int(request.POST.get("emp_department"))

        # create model object and set the data
        e=Employee()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        # e.dept=emp_department
        e.dept_id = emp_department
        if emp_working is None:
            e.working=False

        e.save()
        return redirect("/")
    
    depts=Department.objects.all()
    return render(request,"employee/addEmp.html",{
        'depts': depts
    })

def delEmp(request,emp_id):
    # print(emp_id)
    emp=Employee.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/")

def updateEmp(request,emp_id):

    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=int(request.POST.get("emp_department"))
    
        e=Employee.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        # e.department=emp_department
        e.dept_id = emp_department

        if emp_working is None:
            e.working=False
        else:
            e.working=True

        e.save()
        return redirect("/")

    emp=Employee.objects.get(pk=emp_id)
    depts=Department.objects.all()
    return render(request,"employee/updateEmp.html",{
        'emp':emp,
        'depts':depts
    })

def filter(request):
    if request.method=="POST":
        search=request.POST.get("searchName")
        
        filterResult=Employee.objects.filter(name__icontains = search)
        # print(filterResult)
        
        return render(request,"employee/home.html",{
            'emps':filterResult
        })
