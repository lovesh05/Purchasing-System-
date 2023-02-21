from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from django.contrib.auth.decorators import login_required

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    if request.user.is_authenticated:
        return(redirect('/menu'))
    else:
        return render(
            request,
            'app/index.html',
            {
                'title':'Home Page',
                'year': datetime.now().year,
            }
        )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Dr. Yeoh.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'ABC System',
            'message':'This application processes ...',
            'year':datetime.now().year,
        }
    )

@login_required
def menu(request):
    check_employee = request.user.groups.filter(name='employee').exists()
    check_PM = request.user.groups.filter(name='Purchasing Manager').exists()
    check_Supervisor = request.user.groups.filter(name='Supervisor').exists()
    check_FM = request.user.groups.filter(name='Finance Manager').exists()
    check_Manager = request.user.groups.filter(name='Manager').exists()
    

    context = {
            'title':'Main Menu',
            'is_employee': check_employee,
            'is_Manager' : check_Manager,
            'is_PM' : check_PM,
            'is_Super' : check_Supervisor,
            'is_FM' : check_FM,
            'year':datetime.now().year,
        }
    context['user'] = request.user

    return render(request,'app/menu.html',context)