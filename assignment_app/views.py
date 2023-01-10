from django.shortcuts import render

# Create your views here.
from django.http import request
from django.shortcuts import render,redirect
from.models import *

# Create your views here.
def insertpageview(request):
    return render (request,"app/insert.html")


#data come from html to view
def insertData(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    adress = request.POST['adress']
    #creating object of model class
    #inserting data into table
    newuser= personal_details.objects.create(firstname=fname,lastname=lname,email=email,contact=contact,adress=adress)
    #after insert render show.html
    return redirect('showpage')


#showpage view
def showpageview(request):
    #select*from table name
    #for fatching all the data from table
    all_data=personal_details.objects.all().order_by('firstname').values()# all data sorted with first_name in output response
    return render(request,"app/show.html",{'key1': all_data})

#edit page view
def Editpageview(request,pk):
    #fatching data by perticular id
    get_data=personal_details.objects.get(id = pk)
    return render(request,"app/edit.html",{'key2':get_data})

def updatedata(request,pk):
    udata=personal_details.objects.get(id=pk)
    udata.firstname=request.POST['fname']
    udata.lastname=request.POST['lname']
    udata.email=request.POST['email']
    udata.contact=request.POST['contact']
    udata.adress=request.POST['adress']

    #quary for update
    udata.save()
    return redirect('showpage')


#delete data view

def deletedata(request, pk):
    ddata=personal_details.objects.get(id=pk)
    #query for delete
    ddata.delete()
    return redirect('showpage')
