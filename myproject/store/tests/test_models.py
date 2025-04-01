import pytest
from django.core.exceptions import ValidationError

from store.models import Category, Product

@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(name="Электроника", description="Серверы и комплектующие")
    assert category.name == "Электроника"
    assert category.description == "Серверы и комплектующие"

@pytest.mark.django_db
def test_create_product():
    category = Category.objects.create(name="Электроника", description="Серверы и комплектующие")
    product = Product.objects.create(
        name="ARM Server",
        description="Мощный ARM Server",
        price=500.00,
        category=category
    )
    assert product.name == "ARM Server"
    assert product.price == 500.00
    assert product.category == category

@pytest.mark.django_db
def test_update_category():
    category = Category.objects.create(name="Электроника", description="Серверы и комплектующие")
    category.description = "Новые Серверы и комплектующие"
    category.save()
    updated_category = Category.objects.get(id=category.id)
    assert updated_category.description == "Новые Серверы и комплектующие"

@pytest.mark.django_db
def test_update_product():
    category = Category.objects.create(name="Электроника", description="Серверы и комплектующие")
    product = Product.objects.create(
        name="ARM Server",
        description="Мощный ARM Server",
        price=500.00,
        category=category
    )
    product.price = 450.00
    product.save()
    updated_product = Product.objects.get(id=product.id)
    assert updated_product.price == 450.00

@pytest.mark.django_db
def test_delete_category():
    category = Category.objects.create(name="Электроника", description="Серверы и комплектующие")
    category.delete()
    with pytest.raises(Category.DoesNotExist):
        Category.objects.get(id=category.id)

@pytest.mark.django_db
def test_delete_product():
    category = Category.objects.create(name="Электроника", description="Серверы и комплектующие")
    product = Product.objects.create(
        name="ARM Server",
        description="Мощный ARM Server",
        price=500.00,
        category=category
    )
    product.delete()
    with pytest.raises(Product.DoesNotExist):
        Product.objects.get(id=product.id)

@pytest.mark.django_db
def test_product_negative_price_validation():
    category = Category.objects.create(name="Электроника", description="Серверы и комплектующие")
    with pytest.raises(ValidationError):
        product = Product(
            name="ARM Server",
            description="Мощный ARM Server",
            price=-100.00,
            category=category
        )
        product.full_clean()

