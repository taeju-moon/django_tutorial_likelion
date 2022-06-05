from django.shortcuts import render

def productlist(request):
    return render(request, "product.html")

def productfirst(request):
    return render(request, "productfirst.html")