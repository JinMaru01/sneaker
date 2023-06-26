from django.shortcuts import render, redirect
from .models import Product, Users, Team, Contact
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'Inv/Home.html')

@login_required(login_url='/home')
def team(request):
    teams = Team.objects.all().order_by('StudentId')
    return render(request, 'Inv/Team.html', {'teams': teams})

@login_required(login_url='/home')
def contact(request):
    return render(request, 'Inv/Contact.html')

@login_required(login_url='/home')
def products(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'Inv/Product.html', {'products': products})

@login_required(login_url='/home')
def about(request):
    return render(request, 'Inv/About.html')

@login_required(login_url='/dashboard')
def dashboardProduct(request):
    products = Product.objects.all().order_by('name')
    teams = Team.objects.all().order_by('StudentId')
    return render(request, 'Dashboard/product.html', {'products': products, 'teams': teams})

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'Dashboard/dashboard.html', {'name': 'Dashboard'})

@login_required(login_url='dashboard')
def admins(request):
    users = User.objects.all()
    return render(request, 'Dashboard/admins.html', {'name': 'Admins', 'users': users})

@login_required(login_url='/dashboard')
def inbox(request):
    return render(request, 'Dashboard/inbox.html', {'name': 'Inbox'})


@login_required(login_url='/dashboard')
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
        return render(request, 'Dashboard/addProduct.html')

@login_required(login_url='/dashboard')
def addTeam(request):
    if request.method == 'POST':
        name = request.POST['name']
        StudentId = request.POST['StudentId']
        social = request.POST['facebook']
        description = request.POST['description']
        image = request.FILES['image']

        team = Team(name=name, StudentId=StudentId, social=social, description=description, image=image)
        team.save()
        return redirect('/AddProduct')

    else:
        return render(request, 'Dashboard/addTeam.html')

@login_required(login_url='/dashboard')
def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/Product")

@login_required(login_url='/dashboard')
def destroyTeam(request, id):
    team = Team.objects.get(id=id)
    team.delete()
    return redirect("/Product")

@login_required(login_url='/dashboard')
def destroyAdmin(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/admins")

@login_required(login_url='/dashboard')
def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'Dashboard/edit.html', {'product': product})

@login_required(login_url='/dashboard')
def editTeam(request, id):
    team = Team.objects.get(id=id)
    return render(request, 'Dashboard/editTeam.html', {'team': team})

@login_required(login_url='/dashboard')
def editAdmin(request, id):
    user = User.objects.get(id=id)
    return render(request, 'Dashboard/editAdmin.html', {'user': user})

@login_required(login_url='/dashboard')
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

@login_required(login_url='/dashboard')
def updateTeam(request, id):
    if request.method == 'POST':
        team = Team.objects.get(id=id)
        team.name = request.POST['name']
        team.StudentId = request.POST['StudentId']
        team.social = request.POST['facebook']
        team.description = request.POST['description']

        # Check if a new image file is provided
        if 'image' in request.FILES:
            team.image = request.FILES['image']

        team.save()
        return redirect('/Product')

    else:
        team = Team.objects.get(id=id)
        return render(request, 'Dashboard/editTeam.html', {'team': team})

@login_required(login_url='/dashboard')
def updateAdmin(request, id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.is_superuser =  bool(request.POST.get('isAdmin'))

        user.save()
        return redirect('/admins')

    else:
        user = User.objects.get(id=id)
        return render(request, 'Dashboard/editAdmin.html', {'user': user})

def user_logout(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/dashboard')
def get_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product_data = {
            'id': product.id,
            'name': product.name,
            'image': product.image.url,  # Assuming you have an ImageField in the Product model
            'description': product.description,
            'price': product.price,
        }
        return JsonResponse(product_data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['Confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken. Please use a different email.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('/login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'Inv/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/dashboard/')
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'Inv/login.html', {'error': error_message})

    return render(request, 'Inv/login.html', {'name': 'Login'})

@login_required(login_url='/dashboard')
def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            products = Product.objects.filter(name__icontains=query)
            if products:
                return render(request, 'Inv/SearchBar.html', {'products': products})
            else:
                no_results_message = "No products found matching your search."
                return render(request, 'Inv/SearchBar.html', {'no_results_message': no_results_message})
        else:
            print("No information to show")
    return render(request, 'Inv/SearchBar.html', {})

@login_required(login_url='/dashboard')
def search_members(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            teams = Team.objects.filter(name__icontains=query)
            if teams:
                return render(request, 'Inv/SearchTeam.html', {'teams': teams})
            else:
                no_results_message = "No teams found matching your search."
                return render(request, 'Inv/SearchTeam.html', {'no_results_message': no_results_message})
        else:
            print("No information to show")
    return render(request, 'Inv/SearchTeam.html', {})


# def add_contact(request):
#     if request.method == 'POST':
#         phoneNumber = request.POST.get('phoneNumber')
#         message = request.POST.get('message')
#         username = request.POST.get('username')

#         contact = Contact(username=username, phoneNumber=phoneNumber, message=message)
#         contact.save()
#         return redirect('/AddContact')

#     else:
#         return render(request, 'Dashboard/Contact.html')

def add_contact(request):
    if request.method == 'POST':
        phoneNumber = request.POST.get('phoneNumber')
        message = request.POST.get('message')
        username = request.POST.get('username')

        contact = Contact(username=username, phoneNumber=phoneNumber, message=message)
        contact.save()
        return redirect('/addComment')
    else:
        return render(request, 'Inv/Contact.html')

def view_comments(request):
    contact = Contact.objects.all().order_by('id')
    return render(request, 'Dashboard/ViewComment.html', {'contacts': contact})
