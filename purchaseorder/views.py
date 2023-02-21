from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import *
# Create your views here.

@login_required
def createPOform(request):
    
    newpo_id = PurchaseOrder.objects.latest('poID').poID +1
    quotationList = Quotation.objects.filter(quotationStatus='APPROVED', isPO = False)
    
    context = {
        'title': 'Create Purchase Order Form',
        'year': datetime.now().year,
        'quotationList' : quotationList,
        'newpo_id' : newpo_id,
    }
    context['user'] = request.user

    return render(request,'purchaseorder/createPO.html',context)

def createPOconfirmation(request):
    newpo_date = request.POST.get('poDate')
    newpovalid_date = request.POST.get('poValidDate')
    quotation_object = Quotation.objects.get(quotationID=request.POST.get('quotationID'))
    quotation_products = quotation_object.productID.all()
    
    new_po = PurchaseOrder.objects.create(
        purchaserID = quotation_object.purchaserID, 
        vendorID = quotation_object.vendorID,
        poDate = newpo_date,
        poValidDate = newpovalid_date,
        orderSubtotal = quotation_object.totalPrice,
    )

    for product in quotation_products:
        newpo_item = PurchaseOrderItem.objects.create(
            itemName = product.productName,
            itemQtyNeeded = product.productQtyProvided,
            itemPricePerUnit = product.productPricePerUnit,
            itemPrice = product.productTotalPrice,

        )
        new_po.itemID.add(newpo_item)
        new_po.save()
    quotation_object.isPO = True
    quotation_object.save()

    if request.method == 'POST':

        quotationList = Quotation.objects.all()

    context = {

        # 'poID' : newpoID,
        # 'poValidDate' : newpoValidDate,
        # 'poApprovalStatus' : newpoApprovalStatus,
        # 'poDate' : newpoDate,
        # 'orderSubtotal' : neworderSubtotal,
        'quotationList' : quotationList,
        'new_po' : new_po,
   
    }
    return render(request,'purchaseorder/createPOconfirmation.html',context)

def viewPOlist(request):
    PO_list = PurchaseOrder.objects.all()
    context = {
        'title': 'View Purchase Order',
        'year': datetime.now().year,
        'PO_list' : PO_list,
    }
    context['user'] = request.user

    return render(request,'purchaseorder/viewPOlist.html',context)

def approvePOlist(request):

    PO_list = PurchaseOrder.objects.all()
    context = {
        'PO_list' : PO_list,
    }
    
    return render(request,'purchaseorder/approvePOlist.html',context)

def viewPOdetails(request, po_id):

    po_object = PurchaseOrder.objects.get(pk=po_id)
    items = po_object.itemID.all()

    context = {
        'po_object' : po_object,
        'items' : items
    }

    return render(request,'purchaseorder/viewPOdetails.html',context)

def approvePO(request, po_id):

    po_object = PurchaseOrder.objects.get(pk=po_id)
    po_object.poApprovalStatus = 'APPROVED'
    po_object.save()
    context = {
        'po_object' : po_object,

    }

    return render(request,'purchaseorder/approvedpo.html',context)

def viewapprovedPOlist(request):

    poList = PurchaseOrder.objects.filter(poApprovalStatus='APPROVED')
    context = {
        'poList' : poList,
    }
    
    return render(request,'purchaseorder/viewapprovedPOlist.html',context)
