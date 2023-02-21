from django.contrib import admin
from app.models import *

admin.site.register(Item)
admin.site.register(Purchaser)
admin.site.register(Vendor)
admin.site.register(QuotationProduct)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItem)
admin.site.register(Quotation)