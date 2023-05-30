from django.shortcuts import render,redirect
from .models import Product,CustomUser
from django.http import HttpResponse
from django.db import connection
from django.core.files.storage import default_storage


def home(request):
    return render(request, 'Inv/Home.html')


def contact(request):
    return render(request,'Inv/Contact.html')

def products(request):
    products = Product.objects.all()
    return render(request,'Inv/Product.html', {'products': products})

def about(request):
    return render(request,'Inv/About.html')

def dashboardProduct(request):
    products = Product.objects.all()
    return render(request, 'Dashboard/product.html',{'products': products})

def login(request):
    return render(request,'Inv/Login.html', {'name': 'Sneaker'})

def dashboard(request):
    return render(request,'Dashboard/dashboard.html', {'name': 'Dashboard'})

def admins(request):
    return render(request,'Dashboard/admins.html', {'name': 'Admin'})

def inbox(request):
    return render(request,'Dashboard/inbox.html', {'name': 'Inbox'}) 

def addProduct(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        description = request.POST['description']
        image = request.FILES['image']

        product = Product(name=name, price=price, quantity=quantity, description=description, image=image)
        product.save()
        return redirect('/Product')
    
    else:
        return render(request, 'Dashboard/addProduct.html', {'name': 'Add Product'})

def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/Product") 

def edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'Dashboard/edit.html', {'product':product}) 

def update(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        product.description = request.POST['description']
        
        # Check if a new image file is provided
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        
        product.save()
        return redirect('/Product')
    
    else:
        product = Product.objects.get(id=id)
        return render(request, 'Dashboard/edit.html', {'product': product})
    

def loginAction(request,username,password):
    user = CustomUser.objects.get(username=username,password=password)

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

    return render(request,'Inv/Login.html')

def signAction(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user = CustomUser(username=username, email=email, password=password, confirm_password=confirm_password)
        user.save()
        return redirect('/register')

    return render(request,'Inv/Login.html')

