from django.core.management.base import BaseCommand
from store.models import Product
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Удаление продуктов, созданных более 30 дней назад'

    def handle(self, *args, **kwargs):
        # Вычисляем дату 30 дней назад
        thirty_days_ago = timezone.now() - timedelta(days=30)
        # Удаляем продукты, созданные более 30 дней назад
        deleted_count, _ = Product.objects.filter(created_at__lt=thirty_days_ago).delete()
        self.stdout.write(self.style.SUCCESS(f'Удалено {deleted_count} устаревших продуктов.'))

