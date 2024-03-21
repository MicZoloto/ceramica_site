import csv
from urllib import response
from django.shortcuts import redirect, render
from django.views.generic import FormView
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import FormView
from product.models import SubCategory, Product, Producer
from .forms import ExportCsvForm, ImportCsvForm

class ExportData(FormView):
    """Представлення для експорту CSV-файлу"""
    template_name = 'data_import_export/export_data.html'
    form_class = ExportCsvForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sub_categories'] = SubCategory.objects.all()
        return context

    def form_valid(self, form):
        """Обробка валідної форми"""
        # Отримання даних з форми
        products = form.get_products()

        # Кодування CSV-файлу
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        writer = csv.writer(response)
        # Запис заголовків
        writer.writerow([
            "Назва товару",
            "Розділ",
            "Виробник",
            "Ціна товару",
            "Зображення товару",
            "Артікль",
        ])

        # Запис даних
        for product in products:
            writer.writerow([
                product.name,
                product.sub_category.name,
                product.producer.name,
                product.price,
                product.image,
                product.article,
            ])

        messages.success(self.request, "CSV-файл успішно експортовано.")
        return response


def import_data(request):
    if request.method == 'POST':
        form = ImportCsvForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:
                # Отримує дані з кожного рядка та створює новий об'єкт продукту
                name = row['Назва товару']
                sub_category_name = row['Розділ']
                producer_name = row['Виробник']
                price = row['Ціна товару']
                image = row['Зображення товару']
                article = row['Артікль']

                # Знаходить або створює підкатегорію та виробника
                sub_category, _ = SubCategory.objects.get_or_create(name=sub_category_name)
                producer, _ = Producer.objects.get_or_create(name=producer_name)

                # Створення нового продукту та зберігайте його у базі даних
                product = Product.objects.create(
                    name=name,
                    sub_category=sub_category,
                    producer=producer,
                    price=price,
                    image=image,
                    article=article
                )
                product.save()

            # Оповіщення про успішний імпорт
            messages.success(request, "CSV-файл успішно імпортовано.")
            return redirect('/')
    else:
        form = ImportCsvForm()
    return render(request, 'data_import_export/import_data.html', {'form': form})

