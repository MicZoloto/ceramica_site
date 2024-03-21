from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('export/', views.ExportData.as_view(), name='export_data'),
    path('import/', views.import_data, name='import_data'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)