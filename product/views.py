from django.shortcuts import redirect, render
from .models import Product, Category, Producer, SubCategory
from .forms import ProductForm, CategoryForm, SubCategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    product = Product.objects.all()
    category = Category.objects.all()
    sub_category = SubCategory.objects.all()
    produscer = Producer.objects.all()
    context = {
        "product": product,
        "category": category,
        "produscer": produscer,
        "sub_category": sub_category,
    }
    return render(request, 'product/index.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug) # Отримання категорії за його унікальним ідентифікатором (primary key).
    sub_category = SubCategory.objects.filter(category=category)
    product = Product.objects.all()
    product_count = product.count()  # Кількість всіх об'єктів

    if product.exists():
        product_count = product.count() 
        if product_count > 9:  
            paginator = Paginator(product, 9)  
            page_number = request.GET.get('page')
            
            try:
                page_obj = paginator.page(page_number)
            except PageNotAnInteger:
                page_obj = paginator.page(1)
            except EmptyPage:
                page_obj = paginator.page(paginator.num_pages)
            context = {
                "product": product,
                "category": category,
                "sub_category": sub_category,
                "page_obj": page_obj,
            }
        else:
            context = {
                "product": product,
                "category": category,
                "sub_category": sub_category,
            }
    else:
        context = {
            "product": None,
            "category": category,
            "sub_category": sub_category,
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
        form = ProductForm(request.POST, request.FILES)
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
        form = ProductForm(request.POST, request.FILES, instance=product)
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
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form":form,
        } 
    return render(request, 'product/add_category_form.html', context)

@login_required(login_url='login')
def updateCategory(request, slug):
    category = Category.objects.get(slug=slug)    
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
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

@login_required(login_url='login')
def addSubCategory(request):
    form = SubCategoryForm()
    
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form":form,
        } 
    return render(request, 'product/add_subcategory_form.html', context)

@login_required(login_url='login')
def updateSubCategory(request, slug):
    category = SubCategory.objects.get(slug=slug)    
    form = SubCategoryForm(instance=category)
    if request.method == 'POST':
        form = SubCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form":form,
        } 
    return render(request, 'product/add_subcategory_form.html', context)

@login_required(login_url='login')
def deleteSubCategory(request, slug):
    category = SubCategory.objects.get(slug=slug)
    if request.method == 'POST':
        category.delete()
        return redirect('index')

    context = {
        "SubCategory": category,
    }
    return render(request, 'product/delete-subcategory.html', context)

def loginInstructions(request):
    return render(request, 'product/login-instructions.html')