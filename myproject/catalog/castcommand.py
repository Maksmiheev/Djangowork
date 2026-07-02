from django.core.management.base import BaseCommand
from myproject.catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур'

    def handle(self, *args, **options):
        # Очищаем БД
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загружаем фикстуры
        from django.core.management import call_command
        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'products.json')

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены!'))