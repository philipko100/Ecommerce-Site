from django import forms
from store.models import Category, Product, ProductType


# needs existing  category, and one product image (which will be featured)
class ProductAddForm(forms.ModelForm):
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
    is_on_sale = forms.BooleanField(label='Is this Product on sale?', initial=False, required=False)
    featured_image = forms.ImageField(label='Provide Product Image',)
    class Meta:
        model = Product
        fields = ('category', 'description', 'regular_price', 'discount_price', 'is_on_sale')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'title'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'description'})

class CategoryAddForm(forms.ModelForm):
    name = forms.CharField(label='Enter Category Name', help_text="Required", max_length=255)
    class Meta:
        model = Product
        fields = ('name',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'name'})
