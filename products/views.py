from django.shortcuts import render,HttpResponse
from .models import Product

# Create your views here.

def products_index(request):
    all_products=Product.objects.all()
    
    if 'product_query' in request.GET:
        query=request.GET["product_query"]
        all_products=Product.objects.filter(product_name=query)
    contex={
        "products":all_products
    }
    return render(request,'product_index.html',context=contex)

def update_form(request,id):
    current_obj=Product.objects.get(id=id)
    print(current_obj)
    context={
        "action":"update",
        "product":current_obj
    }
    return render(request,'update_products.html',context=context)

def add_form(request):
    context={
        "action":"add"
    }
    return render(request,'add_products.html',context=context)

def post_add_product(request):
    name=request.POST['name']
    price=request.POST['price']
    category=request.POST['category']
    

   

    add_product=Product( product_name=name,product_price=price, product_category=category)
    add_product.save()

    return HttpResponse("<h2>Product Added</h2>")


def post_update_product(request,id):
    name=request.POST['name']
    price=request.POST['price']
    category=request.POST['category']
   
    update_product=Product.objects.get(id=id)
    update_product.product_name=name
    update_product.product_price=price
    update_product.product_category=category
    
    update_product.save()

    return HttpResponse("<h2>Product Updated</h2>")

def delete(request,id):
    product=Product.objects.get(id=id)
    product.delete()

    return HttpResponse("<h2>Deleted</h2>")