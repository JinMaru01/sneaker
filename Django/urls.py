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

    path('',views.home),
    path('contact/',views.contact),
    path('products/',views.products),
    path('about/',views.about),
    path('login/',views.loginAction),
    path('register/',views.signAction),
    path('AddProduct/',views.addProduct),
    path('Product/',views.dashboardProduct),
    path('dashboard/',views.dashboard),
    path('admins/',views.admins, name='admin'),
    path('inbox/',views.inbox),
    path('delete/<int:id>', views.destroy, name='destroy'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'), 
    path('logout/',views.LogoutPage,name='logout'),
    path('editAdmin/<int:id>', views.editAdmin, name='editAdmin'),
    path('updateAdmin/<int:id>', views.updateAdmin, name='updateAdmin'), 
    path('deleteAdmin/<int:id>', views.destroyAdmin, name='destroy'),
    path('get/product/<int:product_id>/', views.get_product, name='get_product'),

]
