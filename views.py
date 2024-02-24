from django.shortcuts import render, get_object_or_404
from .models import Product, ARSession

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def activate_ar(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'activate_ar.html', {'product': product})

def complete_ar_try_on(request, product_id):
    # Handle the completion of AR Try-On, e.g., add to cart logic
    return render(request, 'complete_ar_try_on.html')
