from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category


class Command(BaseCommand):
    help = 'Добавляет тестовую категорию в БД'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Данные "Категория" успешно загружены из фикстуры'))