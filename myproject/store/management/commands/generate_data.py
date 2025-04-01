from django.core.management.base import BaseCommand
from store.models import Category, Product
import random
from django.utils import timezone

class Command(BaseCommand):
    help = 'Генерация тестовых данных для категорий и продуктов'

    def handle(self, *args, **kwargs):
        # Создаём 5 категорий
        for i in range(5):
            category = Category.objects.create(
                name=f'Категория {i+1}',
                description=f'Описание категории {i+1}',
            )
            # Создаём 10 продуктов для каждой категории
            for j in range(10):
                Product.objects.create(
                    name=f'Продукт {j+1} категории {i+1}',
                    description=f'Описание продукта {j+1}',
                    price=random.randint(100, 1000),
                    category=category,
                    created_at=timezone.now(),
                )
        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно созданы!'))

