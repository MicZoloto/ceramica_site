from django.shortcuts import redirect, render
from .models import Product, Category, Producer, SubCategory
from .forms import ProductForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()
    produscer = Producer.objects.all()
    menu = Category.objects.all()
    context = {
        "product": product,
        "category": category,
        "produscer": produscer,
        "sub_category": sub_category,
        "menu": menu,
    }
    return render(request, 'product/index.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug) # Отримання категорії за його унікальним ідентифікатором (primary key).
    sub_category = SubCategory.objects.filter(category=category)
    product = Product.objects.all()
    menu = Category.objects.all()
    context = {
        "product": product,
        "category": category,
        "sub_category": sub_category,
        "menu": menu,
    }
    return render(request, 'product/category.html', context)

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.warning(request, 'Користувача не існує')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, 'Логін чи пароль не дійсні')

    return render(request, 'product/login-instructions.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'Ви вийшли')
    return redirect('/')    

@login_required(login_url='login')
def addProduct(request):
    form = ProductForm()
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form":form,
        } 
    return render(request, 'product/add_product_form.html', context)

@login_required(login_url='login')
def updateProduct(request, id):
    product = Product.objects.get(id=id)    
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form":form,
        } 
    return render(request, 'product/add_product_form.html', context)

@login_required(login_url='login')
def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')

    context = {
        "product": product,
    }
    return render(request, 'product/delete-product.html', context)


@login_required(login_url='login')
def addCategory(request):
    form = CategoryForm()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form":form,
        } 
    return render(request, 'product/add_category_form.html', context)

@login_required(login_url='login')
def updateCategory(request, slug):
    product = Category.objects.get(slug=slug)    
    form = CategoryForm(instance=product)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form":form,
        } 
    return render(request, 'product/add_category_form.html', context)

@login_required(login_url='login')
def deleteCategory(request, slug):
    category = Category.objects.get(slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('index')

    context = {
        "category": category,
    }
    return render(request, 'product/delete-category.html', context)

def loginInstructions(request):
    return render(request, 'product/login-instructions.html')
