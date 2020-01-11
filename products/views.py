from django.shortcuts import render,HttpResponse
from .models import Product
from django.core.files.storage import FileSystemStorage
# Create your views here.

def products_index(request):
    all_products=Product.objects.all()
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
    image=request.FILES["product_image"]

    fs=FileSystemStorage()
    filename=fs.save(image.name,image)
    urls=fs.url(filename)


    add_product=Product(product_name=name,product_price=price,product_category=category,product_image=urls)

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