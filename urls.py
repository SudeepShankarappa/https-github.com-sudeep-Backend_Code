from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('activate-ar/<int:product_id>/', views.activate_ar, name='activate_ar'),
    path('complete-ar-try-on/<int:product_id>/', views.complete_ar_try_on, name='complete_ar_try_on'),
]
