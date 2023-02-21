"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User

#sharing entity
def get_vendorID():
    return Vendor.vendorID

def get_purchaserID():
    return Purchaser.purchaserID

def get_quotationID():
    return Quotation.quotationID

def get_poID():
    return PurchaseOrder.poID

def get_productID():
    return QuotationProduct.productID

class Item(models.Model):
    item_id = models.CharField(primary_key=True, max_length=10)
    item_name = models.TextField()
    item_description = models.TextField(null=True,default=None, blank=True)
    def __str__(self):
        return str(self.item_id)


class Purchaser(models.Model):
    purchaserID = models.AutoField(primary_key=True)
    purchaserAddress = models.CharField(max_length=50)
    purchaserContact = models.BigIntegerField()
    purchaserName = models.CharField(max_length=30)
    purchaserCompanyName = models.CharField(max_length=30)
    def __str__(self):
        return str(self.purchaserID)

class Vendor(models.Model):
    vendorID = models.AutoField(primary_key=True)
    vendorName = models.CharField(max_length=20)
    vendorContact = models.BigIntegerField()
    vendorAddress = models.CharField(max_length=50)
    vendorCompanyName = models.CharField(max_length=30)

    # totalproductPricePerUnit = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.vendorID)

class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "pending"),
        ("APPROVED", "approved"),
        ("REJECTED", "rejected")
    )
    poID = models.AutoField(primary_key=True)
    purchaserID = models.ForeignKey(Purchaser, on_delete=models.SET(get_purchaserID))
    vendorID = models.ForeignKey(Vendor, on_delete=models.SET(get_vendorID))
    poValidDate = models.DateField(max_length=10)
    poApprovalStatus = models.CharField(default='PENDING', choices=STATUS_CHOICES, max_length=10)
    poDate = models.DateField(max_length=10)
    itemID = models.ManyToManyField('PurchaseOrderItem', blank=True)
    # quotationID = models.ForeignKey(Quotation, on_delete=models.SET(get_quotationID))
    orderSubtotal = models.DecimalField(max_digits=10, decimal_places=2)   
    def __str__(self):
        return str(self.poID) 

class QuotationProduct(models.Model):
    productID = models.AutoField(primary_key=True)
    # quotationID = models.ForeignKey(Quotation, on_delete=models.SET(get_quotationID))
    purchaserID = models.ForeignKey(Purchaser, on_delete=models.SET(get_purchaserID), null=True)
    vendorID = models.ForeignKey(Vendor, on_delete=models.SET(get_vendorID))
    productName = models.CharField(max_length=30)
    productQtyProvided = models.IntegerField()
    productPricePerUnit = models.DecimalField(max_digits=10, decimal_places=2)
    productTotalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.productID)

class PurchaseOrderItem(models.Model):
    itemID = models.AutoField(primary_key=True)
    # poID = models.ForeignKey(PurchaseOrder, on_delete=models.SET(get_poID))
    # productID = models.ForeignKey(QuotationProduct, on_delete=models.SET(get_productID), null=True)
    itemName = models.CharField(max_length=10)
    itemQtyNeeded = models.IntegerField()
    itemPricePerUnit = models.DecimalField(max_digits=10, decimal_places=2)
    itemPrice = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.itemID)

class Quotation(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "pending"),
        ("APPROVED", "approved"),
    )
    quotationID = models.AutoField(primary_key=True)
    quotationStatus = models.CharField(default='PENDING', choices=STATUS_CHOICES, max_length=10)
    quotationDate = models.DateField(max_length=10)
    quotationValidDate = models.DateField(max_length=10)
    purchaserID = models.ForeignKey(Purchaser, on_delete=models.SET(get_purchaserID))
    vendorID = models.ForeignKey(Vendor, on_delete=models.SET(get_vendorID))
    productID = models.ManyToManyField(QuotationProduct, null=True)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    isPO = models.BooleanField(default=False) 
    def __str__(self):
        return str(self.quotationID)
