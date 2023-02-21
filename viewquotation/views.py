from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import *
# Create your views here.

@login_required
def viewquotation(request):
    quotation_list = Quotation.objects.all()
    quotation_ids = Quotation.objects.all().order_by('quotationID')
    context = {
        'title': 'View Quotation',
        'year': datetime.now().year,
        'quotation_list' : quotation_list,
        'quotation_ids' : quotation_ids,
    }
    context['user'] = request.user

    return render(request,'viewquotation/viewquotation.html',context)

