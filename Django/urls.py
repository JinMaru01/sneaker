"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Config import views
from django.contrib.auth import authenticate

urlpatterns = [

    path('',views.home,name='home'),
    path('contact/',views.contact),
    path('products/',views.products),
    path('about/',views.about),
    path('login/',views.user_login),
    path('team/',views.team),
    
    path('register/',views.register),
    path('AddProduct/',views.addProduct, name = 'Add Product'),
    path('AddTeam/',views.addTeam, name = 'Add Team'),
    path('Product/',views.dashboardProduct),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('admins/',views.admins, name='admin'),
    path('inbox/',views.inbox),
    path('delete/<int:id>', views.destroy, name='destroy'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'), 

    path('deleteTeam/<int:id>', views.destroyTeam, name='destroy'),
    path('editTeam/<int:id>', views.editTeam, name='edit'),
    path('updateTeam/<int:id>', views.updateTeam, name='update'), 

    path('search/', views.searchBar, name='search'),
    path('searchTeam/', views.search_members, name='searchMember'),
    path('logout/',views.user_logout,name='logout'),
    path('editAdmin/<int:id>', views.editAdmin, name='editAdmin'),
    path('updateAdmin/<int:id>', views.updateAdmin, name='updateAdmin'), 
    path('deleteAdmin/<int:id>', views.destroyAdmin, name='destroy'),
    path('get/product/<int:product_id>/', views.get_product, name='get_product'),

    path('addComment/', views.add_contact, name = 'add_contact'),
    path('ViewComment/', views.view_comments, name = 'view_comments'),

]
