from random import random

from account.models import UserBase
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Category, Product, ProductImage, ProductType

from inventory.forms import CategoryAddForm, ProductAddForm
from inventory.models import InventoryItem


def inventory_summary(request):
    inventoryItems = InventoryItem.objects.filter(user=request.user.id)
    products = []
    for inventory in inventoryItems:
        products.append(inventory.product)
    return render(request, 'inventory/summary.html', {'products' : products})

# assumes that category exist and is taken care of
def inventory_add(request):
    if request.method == 'POST':
        product_add_form = ProductAddForm(request.POST, request.FILES)
        if product_add_form.is_valid():
            titleString = str(product_add_form.cleaned_data['title'])
            titleString = titleString.lower()
            slug = titleString.replace(" ", "-")
            product = Product.objects.create(
                category=product_add_form.cleaned_data['category'],
                title=product_add_form.cleaned_data['title'],
                description=product_add_form.cleaned_data['description'],
                slug=slug,
                regular_price=product_add_form.cleaned_data['regular_price'],
                discount_price=product_add_form.cleaned_data['discount_price'],
                is_on_sale=product_add_form.cleaned_data['is_on_sale'],
                is_active=True,
            )
            user_id = request.user.id
            user = UserBase.objects.get(pk=user_id)
            InventoryItem.objects.create(
                user=user,
                product=product,
            )
            image = ProductImage.objects.create(
                product=product,
                image=product_add_form.cleaned_data['featured_image'],
                is_feature=True,
            )
            image.save()
            return render(request, 'inventory/product_added.html')
    else:
        product_add_form = ProductAddForm()
    return render(request, 'inventory/add_product_inventory.html', {'form': product_add_form})

# assumes that category exist and is taken care of
def inventory_edit(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        product_add_form = ProductAddForm(request.POST, request.FILES)
        if product_add_form.is_valid():
            Product.objects.filter(pk=id).update(
                category=product_add_form.cleaned_data['category'],
                title=product_add_form.cleaned_data['title'],
                description=product_add_form.cleaned_data['description'],
                regular_price=product_add_form.cleaned_data['regular_price'],
                discount_price=product_add_form.cleaned_data['discount_price'],
                is_on_sale=product_add_form.cleaned_data['is_on_sale'],
            )
            ProductImage.objects.filter(product=product).filter(is_feature=True).update(is_feature=False)
            image = ProductImage.objects.create(
                product=product,
                image=product_add_form.cleaned_data['featured_image'],
                is_feature=True,
            )
            image.save()
            return render(request, 'inventory/product_added.html')
    else:
        product_add_form = ProductAddForm(instance=product)
    return render(request, 'inventory/add_product_inventory.html', {'form': product_add_form})

def inventory_inactive(request, id):
    Product.objects.filter(pk=id).update(is_active = False)
    return redirect("inventory:inventory_summary")

def inventory_delete(request, id):
    Product.objects.filter(pk=id).delete()
    return redirect("inventory:inventory_summary")


def category_add(request):
    if request.method == 'POST':
        category_add_form = CategoryAddForm(request.POST)
        if category_add_form.is_valid():
            nameString = str(category_add_form.cleaned_data['name'])
            nameString = nameString.lower()
            slug = nameString.replace(" ", "-")
            Category.objects.create(
                name=category_add_form.cleaned_data['name'],
                slug=slug,
                is_active=True,
            )
            return render(request, 'inventory/product_added.html')
    else:
        category_add_form = CategoryAddForm()
    return render(request, 'inventory/add_product_category.html', {'form': category_add_form})
