from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import UserForm,CategoryForm,ProductForm,SubCategoryForm,CustomAuthenticationForm
from django.contrib.auth.decorators import login_required


from .models import Categoria,Producto,SubCategoria

def subCategory_delete(request,id):
   subCategory = get_object_or_404(SubCategoria,pk=id)
   if(request.method == "POST"):
    subCategory.delete()
    return redirect('subCategory')

def subCategory_details(request,id):
    if(request.method == "POST"):
        subCategory = get_object_or_404(SubCategoria,pk=id)
        form = SubCategoryForm(request.POST,instance=subCategory)
        if form.is_valid():
            form.save()
            return redirect("subCategory")
    else:
        subCategory = get_object_or_404(SubCategoria,pk=id)
        form =  SubCategoryForm(instance=subCategory)
    return render(request,'subCategory_details.html',{
        'subCategoria': subCategory,
        'form': form
    })

def category_delete(request,id):
    category = get_object_or_404(Categoria,pk=id)
    if(request.method == "POST"):
        category.delete()
        return redirect('category')

def category_details(request,id):
    if(request.method == 'POST'):
        category = get_object_or_404(Categoria,pk=id)
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    else :
        category = get_object_or_404(Categoria,pk=id)
        form =  CategoryForm(instance=category)
    return render(request,'category_details.html',{
        'categoria' : category,
        "form": form
    })

def product_delete(request,id):
    product = get_object_or_404(Producto,pk=id)
    if(request.method == 'POST'):
        product.delete()
        return redirect('products')


def product_details(request,id):

    if request.method == 'POST':
        product = get_object_or_404(Producto,pk=id)
        form = ProductForm(request.POST, request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')  
    else:
        product = get_object_or_404(Producto,pk=id)
        form = ProductForm(instance=product)
    
    return render(request,'product_details.html',{
        'producto' : product,
        'form': form 
    })
    

@login_required
def create_subCategory(request):
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
          
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('subCategory')  
    else:
        form = SubCategoryForm()
    
    return render(request, 'create_sub_category.html', {'form': form})

@login_required
def all_subCategorys(request):
    sub_categories = SubCategoria.objects.all()
    return render(request,'subCategories.html',{
        "sub_categorias" : sub_categories
    })


@login_required
def all_products(request):
    products = Producto.objects.all()
    print(products)
    return render(request,'productos.html',{
        'productos' : products
    })

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
          
            new_product = form.save(commit=False)
            new_product.user = request.user
            new_product.save()
            return redirect('products')  
    else:
        form = ProductForm()
    
    return render(request, 'create_product.html', {'form': form})

    

@login_required
def all_category(request):
    categorias = Categoria.objects.all()
    return render(request,'categorias.html',{
        'categorias': categorias
    })

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():

            new_category = form.save(commit=False)
            new_category.user = request.user
            new_category.save()
            return redirect('category')  
    else:
        form = CategoryForm()
    
    return render(request, 'create_category.html', {'form': form})


def singin(request):

    if(request.method == 'GET'):
        return render(request,'signin.html',{
        'form' : CustomAuthenticationForm
    })
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])

        if( user is None) : 
            return render(request,'signin.html',{
                'form' : CustomAuthenticationForm,
                "error" : "Username or password is incorrect"
                })
        else:
            login(request,user)
            return redirect('products') 
        
    

def signout(request):
    logout(request)
    return redirect('singin')

def menu(request):
    return render(request,'menu.html')



def signup(request):

    form = UserForm()
    if(request.method == 'GET'):
        return render(request,'signup.html',{
        "form":form
        })
    else:
        if(request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password2'])
                user.save()
                login(request,user)
                return redirect('products')
            except IntegrityError:
                return render(request,'signup.html',{
                    "form":form,
                    "error": "Username already exists"
                    })
            

        else:
            return render(request,'signup.html',{
                    "form":form,
                    "error": "Passwords do not match"
                    })
            

   