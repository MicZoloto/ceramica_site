from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from .models import Product, Category, Producer, SubCategory, Page
from .forms import ContactForm, ProductForm, CategoryForm, SubCategoryForm, PageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.cache import cache

def index(request):
    categories = cache.get('category_list')
    if not categories:
        categories = Category.objects.all()
        cache.set('category_list', categories, 60*5)
    
    context = {
        "categories": categories,
    }
    return render(request, 'product/index.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    sub_categories = SubCategory.objects.filter(category=category)
    
    context = {
        "category": category,
        "sub_categories": sub_categories,
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
            messages.info(request, 'Товар додано успішно')
            return redirect('index')
        else:
            messages.warning(request, 'Щось пішло не так! Товар не додано!')

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
            messages.info(request, 'Товар змінено успішно')
            form.save()
            return redirect('index')
        else:
            messages.warning(request, 'Щось пішло не так! Товар не зінено!')

    context = {
        "form":form,
        } 
    return render(request, 'product/add_product_form.html', context)

@login_required(login_url='login')
def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        messages.warning(request, 'Товар видалено успішно!')
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

def subCategory(request, slug):
    sub_category = get_object_or_404(SubCategory, slug=slug)
    products_list = Product.objects.filter(sub_category=sub_category).select_related('sub_category', 'producer')

    # Pagination logic
    paginator = Paginator(products_list, 9)  # 9 products per page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "sub_category": sub_category,
        "products": products,
    }
    
    return render(request, 'product/sub-category.html', context)

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

def pages(request, slug):
    pages = Page.objects.get(slug=slug)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Повідомлення з сайту ceramica_site від {name} ({email})',
                message,
                email,
                ['mic.zoloto@gmail.com'],  # Адреса, куди надсилати повідомлення
                fail_silently=False,
            )
            return redirect('page', slug=slug)
    else:
        form = ContactForm()

    context = {
        "page": pages,
        'form': form
    }
    return render(request, 'product/page.html', context)

@login_required(login_url='login')
def updatePages(request, slug):
    pages = Page.objects.get(slug=slug)    
    form = PageForm(instance=pages)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=pages)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form":form,
        } 
    return render(request, 'product/edit_page_form.html', context)

def page404(request, exception):
    return render(request, '404.html')