from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import *

# Create your views here.

@login_required
def addvendorform(request):
    context = {
        'title': 'Add Vendor Form',
        'year': datetime.now().year,
    }
    context['user'] = request.user

    return render(request,'addvendor/addvendorform.html',context)

def addvendorconfirmation(request):

    newvendorCompanyName = request.POST['vendorCompanyName']
    newvendorAddress = request.POST['vendorAddress']
    newvendorName = request.POST['vendorName']
    newvendorContact = request.POST['vendorContact']

    newvendor = Vendor(vendorCompanyName = newvendorCompanyName, vendorAddress = newvendorAddress, 
                     vendorName = newvendorName, vendorContact = newvendorContact)
    newvendor.save()

    context = {

        'vendorCompanyName': newvendorCompanyName,
        'vendorAddress' : newvendorAddress,
        'vendorName' : newvendorName,
        'vendorContact' : newvendorContact,
   
    }
    return render(request,'addvendor/addvendorconfirmation.html',context)
