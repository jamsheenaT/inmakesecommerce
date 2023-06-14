from . import views
from django.contrib import admin
from django.urls import path,include
app_name='ecommerceapp'
urlpatterns = [

   path('',views.allprodcat,name='allprodcat'),
   path('<slug:c_slug>/',views.allprodcat,name='product_by_category'),
   path('<slug:c_slug>/<slug:product_slug>/',views.ProDetail,name='prodCatdetail')

]
