"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app import views as main_views
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime


from additem import views as additem_views

# from quotation import views as addquotation

from addvendor import views as addvendor_views

# from viewquotation import views as viewquotation_views

from addquotation import views as addquotation_views

from purchaseorder import views as createPO_views





admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', main_views.home, name='home'),
    re_path(r'^contact$', main_views.contact, name='contact'),
    re_path(r'^about$', main_views.about, name='about'),
    re_path(r'^login/$',
        LoginView.as_view(template_name = 'app/login.html'),
        name='login'),
    re_path(r'^logout$',
        LogoutView.as_view(template_name = 'app/index.html'),
        name='logout'),
    re_path(r'^menu$', main_views.menu, name='menu'),

    re_path(r'^additemform$', additem_views.additemform, name='additem_form'),
    re_path(r'^additemconfirmation$', additem_views.additemconfirmation, name='additem_confirmation'),

    re_path(r'^addvendorform$', addvendor_views.addvendorform, name='addvendor_form'),
    re_path(r'^addvendorconfirmation$', addvendor_views.addvendorconfirmation, name='addvendor_confirmation'),

    path('viewquotationlist', addquotation_views.viewquotationlist, name='viewquotationlist'),
    re_path(r'^addquotation$', addquotation_views.addquotation, name='addquotation_form'),
    path('viewquotationdetails/<int:quotation_id>/',addquotation_views.viewquotationdetails, name='viewquotationdetails'),
    path('approvequotationlist', addquotation_views.approvequotationlist, name='approvequotationlist'),
    path('approvequotation/<int:quotation_id>/',addquotation_views.approvequotation, name='approvequotation'),
    path('viewselectedquotationlist', addquotation_views.viewselectedquotationlist, name='viewselectedquotationlist'),

    re_path(r'^createPOform', createPO_views.createPOform, name='createPO_form'),
    re_path(r'^createPOconfirmation', createPO_views.createPOconfirmation, name='createPO_confirmation'),
    path('viewPOlist', createPO_views.viewPOlist, name='viewPOlist'),
    path('approvePOlist', createPO_views.approvePOlist, name='approvePOlist'),
    path('viewPOdetails/<int:po_id>/',createPO_views.viewPOdetails, name='viewPOdetails'),
    path('approvePO/<int:po_id>/',createPO_views.approvePO, name='approvepo'),
    path('viewapprovedPOlist', createPO_views.viewapprovedPOlist, name='viewapprovedPOlist'),





]
