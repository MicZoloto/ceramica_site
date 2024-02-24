from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>', views.category, name='category'),
    path('add-product/', views.addProduct, name='add-product'),
    path('update-product/<int:id>/', views.updateProduct, name='update-product'),
    path('delete-product/<int:id>/', views.deleteProduct, name='delete-product'),
    path('add-category/', views.addCategory, name='add-category'),
    path('update-category/<slug:slug>/', views.updateCategory, name='update-category'),
    path('delete-product/<slug:slug>/', views.deleteCategory, name='delete-category'),
    path('login/', views.loginUser, name='login'),  
    path('logout/', views.logoutUser, name='logout'),
    path('login-instructions/', views.loginInstructions, name='login-instructions'),
    path('navigations/', views.navigations, name='navigations'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)