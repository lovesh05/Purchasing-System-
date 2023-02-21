from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from app.models import *
import json

# Create your views here.


@login_required
def addquotation(request):
    newquotation_id = Quotation.objects.latest('quotationID').quotationID + 1

    if request.method == 'POST':

        newquotation_date = request.POST.get('quotationDate')
        newquotationvalid_date = request.POST.get('quotationValidDate')
        newquotation_purchaser = Purchaser.objects.get(
            pk=request.POST.get('purchaserID'))
        newquotation_vendor = Vendor.objects.get(
            pk=request.POST.get('vendorID'))
        newquotation_total = request.POST.get('totalPrice')
        products = request.POST.get('products')
        products_array = json.loads(products)

        newquotation = Quotation(quotationDate=newquotation_date, quotationValidDate=newquotationvalid_date, purchaserID=newquotation_purchaser, vendorID=newquotation_vendor,
                                 totalPrice=newquotation_total)
        newquotation.save()
        for product in products_array:
            newquotation.productID.create(productName=product['productName'],
                                          productPricePerUnit=product['productPrice'],
                                          productQtyProvided=product['productQuantity'],
                                          productTotalPrice=product['productTotal'],
                                          vendorID=newquotation_vendor,
                                          purchaserID=newquotation_purchaser)

        newquotation.save()

    purchaserList = Purchaser.objects.all()
    vendorList = Vendor.objects.all()
    productList = QuotationProduct.objects.all()
    context = {
        'purchaserList': purchaserList,
        'vendorList': vendorList,
        'productList': productList,
        'newquotation_id': newquotation_id
    }

    return render(request, 'addquotation/addquotation.html', context)

# def selectquotation(request):


def viewquotationlist(request):

    quotationList = Quotation.objects.all()
    context = {
        'quotationList': quotationList,
    }

    return render(request, 'addquotation/viewquotationlist.html', context)


def viewquotationdetails(request, quotation_id):

    quotation_object = Quotation.objects.get(pk=quotation_id)
    products = quotation_object.productID.all()

    context = {
        'quotation_object': quotation_object,
        'products': products
    }

    return render(request, 'addquotation/viewquotationdetails.html', context)


def addvendorform(request):
    context = {
        'title': 'Add Vendor Form',
        'year': datetime.now().year,
    }
    context['user'] = request.user

    return render(request, 'addvendor/addvendorform.html', context)


def addvendorconfirmation(request):

    newvendorCompanyName = request.POST['vendorCompanyName']
    newvendorAddress = request.POST['vendorAddress']
    newvendorName = request.POST['vendorName']
    newvendorContact = request.POST['vendorContact']

    newvendor = Vendor(vendorCompanyName=newvendorCompanyName, vendorAddress=newvendorAddress,
                       vendorName=newvendorName, vendorContact=newvendorContact)
    newvendor.save()

    context = {

        'vendorCompanyName': newvendorCompanyName,
        'vendorAddress': newvendorAddress,
        'vendorName': newvendorName,
        'vendorContact': newvendorContact,

    }
    return render(request, 'addvendor/addvendorconfirmation.html', context)


def viewPOlist(request):
    PO_list = PurchaseOrder.objects.all()
    context = {
        'title': 'View Purchase Order',
        'year': datetime.now().year,
        'PO_list': PO_list,
    }
    context['user'] = request.user

    return render(request, 'purchaseorder/viewPOlist.html', context)


def viewPOdetails(request, po_id):

    po_object = PurchaseOrder.objects.get(pk=po_id)
    items = po_object.itemID.all()

    context = {
        'po_object': po_object,
        'items': items
    }

    return render(request, 'purchaseorder/viewPOdetails.html', context)


def viewapprovedPOlist(request):

    poList = PurchaseOrder.objects.filter(poApprovalStatus='APPROVED')
    context = {
        'poList': poList,
    }

    return render(request, 'purchaseorder/viewapprovedPOlist.html', context)
