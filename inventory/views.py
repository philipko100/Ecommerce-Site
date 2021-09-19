from account.models import UserBase
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from store.models import Category, Product, ProductImage, ProductType

from inventory.forms import ProductAddForm
from inventory.models import InventoryItem


def inventory_summary(request):
    inventoryItems = InventoryItem.objects.filter(user=request.user.id)
    products = []
    for inventory in inventoryItems:
        products.append(inventory.product)
    return render(request, 'inventory/summary.html', {'products' : products})     # create the templates

# assumes that product type and product specifications exist and is taken care of
def inventory_add(request):
    print("in inventory add")
    if request.method == 'POST':
        print("is post")
        product_add_form = ProductAddForm(request.POST, request.FILES)
        if product_add_form.is_valid():
            print("is valid")
            # product = product_add_form.save(commit=False)
            titleString = str(product_add_form.cleaned_data['title'])
            titleString = titleString.lower()
            slug = titleString.replace(" ", "-")
            product = Product.objects.create(
                product_type=product_add_form.cleaned_data['product_type'],
                category=product_add_form.cleaned_data['category'],
                title=product_add_form.cleaned_data['title'],
                description=product_add_form.cleaned_data['description'],
                slug=slug,
                regular_price=product_add_form.cleaned_data['regular_price'],
                discount_price=product_add_form.cleaned_data['discount_price'],
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
        print("not post")
        product_add_form = ProductAddForm()
    return render(request, 'inventory/add_product_inventory.html', {'form': product_add_form})
