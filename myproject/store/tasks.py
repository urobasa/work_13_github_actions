from celery import shared_task
from django.apps import apps

@shared_task
def log_new_product(product_id):
    Product = apps.get_model('store', 'Product')
    product = Product.objects.get(id=product_id)
    print(f"Новый товар добавлен: {product.name}")

