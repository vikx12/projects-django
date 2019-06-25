from django.shortcuts import render

from django.http import HttpResponse
def hello(request):
    que="Who developed C Language?"
    a="Ken Thompson"
    b="Dennis Ritchi"
    c="Bjarne Stroustrup"
    d="abdaal ahmad"
    e="hello guest"
    Level="this is sucks"
    data={"que":que,"a":a,"b":b,"c":c,"d":d,"e":e,"Level":Level}
    res=render(request,"exam/test.html",context=data)
    return res
def sorry(request):
    s1="<h1>why u cant say sorry</h1>"
    return HttpResponse(s1)
