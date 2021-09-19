from django import forms
from store.models import Category, Product, ProductType


# no product specification for now, needs existing product type and category, and one product image (which will be featured)
class ProductAddForm(forms.ModelForm):
    product_type = forms.ModelChoiceField(label='Enter Product Type', help_text="Required", queryset=ProductType.objects.all())

    category = forms.ModelChoiceField(label='Enter Product Category', help_text="Required", queryset=Category.objects.all())

    title = forms.CharField(label='Enter Product Title', help_text="Required", max_length=255)
    description = forms.CharField(label='Enter Product Description', help_text="Not Required", max_length=255)
    
    regular_price = forms.DecimalField(
        label='Enter Regular Price',
        help_text="Maximum 999.99",
        error_messages={
            "name": {
                "max_length": "The price must be between 0 and 999.99.",
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = forms.DecimalField(
        label='Enter Discounted Price',
        help_text="Maximum 999.99",
        error_messages={
            "name": {
                "max_length": "The price must be between 0 and 999.99.",
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    featured_image = forms.ImageField(label='Provide Product Image',)
    class Meta:
        model = Product
        fields = ('product_type', 'category', 'description', 'regular_price', 'discount_price',)

    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_slug(self):
        return self.slug
    def get_regular_price(self):
        return self.regular_price
    def get_discount_price(self):
        return self.discount_price
