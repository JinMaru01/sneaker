from django.shortcuts import render,redirect
from .models import Product, Users
from django.http import HttpResponse
from django.db import connection
from django.core.files.storage import default_storage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'Inv/Home.html')

# @login_required(login_url='/login/')
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

def dashboard(request):
    return render(request,'Dashboard/dashboard.html', {'name': 'Dashboard'})

def admins(request):
    users = Users.objects.all()
    return render(request,'Dashboard/admins.html', {'name':'Admins','users': users})

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
        return redirect('/AddProduct')
    
    else:
        return render(request, 'Dashboard/addProduct.html', {'name': 'Add Product'})

def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/Product") 

def destroyAdmin(request, id):  
    user = Users.objects.get(id=id)  
    user.delete()  
    return redirect("/admins")

def edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'Dashboard/edit.html', {'product':product}) 

def editAdmin(request, id):  
    user = Users.objects.get(id=id)  
    return render(request,'Dashboard/editAdmin.html', {'user':user}) 

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
    
def updateAdmin(request, id):
    if request.method == 'POST':
        user = Users.objects.get(id=id)
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.isAdmin = request.POST['isAdmin']
        
        user.save()
        return redirect('/admins')
    
    else:
        user = Users.objects.get(id=id)
        return render(request, 'Dashboard/editAdmin.html', {'user': user})

# Rest of your view functions...

def loginAction(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the user exists in the database
        try:
            user = Users.objects.get(username=username)
        except Users.DoesNotExist:
            # Handle invalid login credentials
            error_message = 'User not found'
            return render(request, 'Inv/login.html', {'error': error_message})

        # Compare the password with the user's password from the database
        if password == user.password:
            # Authenticate and log in the user
            if user.isAdmin:
                # Redirect to the dashboard for admins
                return redirect('/dashboard/')
            else:
                # Redirect to the home page for non-admin users
                return redirect('/')
        else:
            # Handle invalid login credentials
            error_message = 'Invalid password'
            return render(request, 'Inv/login.html', {'error': error_message})

    return render(request, 'Inv/login.html', {'name': 'Login'})


def signAction(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('Confirm_password')

        user = Users(
            username=username,
            email=email,
            password=(password),
            confirm_password=(confirm_password),
            isAdmin=False
        )
        user.save()
        return redirect('/login/')

    return render(request, 'Inv/register.html', {'name': 'Signup'})

def LogoutPage(request):
    logout(request)
    return redirect('/login')
