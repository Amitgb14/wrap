from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'product/csr/add/', add_product_csr, name='add_product_csr'),
    url(r'product/add/', add_product, name='add_product'),
    url(r'product/get/', get_product, name='get_product'),

    url(r'^$', dashboard, name='dashboard'),

]
