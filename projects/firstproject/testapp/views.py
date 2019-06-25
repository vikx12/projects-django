from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee

def employees_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    res=render(request,'testapp/hoe.html',data)
    return res
def greeting(request):
    s1="<h1>hello welcome shit fucker</h1>"
    return HttpResponse(s1)
def showcontact(request):
        s1="<h1>this is showcontact page</h1>"
        return HttpResponse(s1)
def about(request):
    text="this is hit"


    return render(request,'testapp/about.html',{'text':text})
