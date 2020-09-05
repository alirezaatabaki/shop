from django import forms
from django.core.exceptions import ValidationError


class CartAddForm(forms.Form):
	quantity = forms.IntegerField(label='تعداد', min_value=1)

	def __init__(self, *args, **kwargs):
		self.product = kwargs.pop('product', None)
		super(CartAddForm, self).__init__(*args, **kwargs)

	def clean_quantity(self):
		quantity = self.cleaned_data.get('quantity')
		if quantity > self.product.quantity:
			raise ValidationError(f'حداکثر تعداد قبال سفارش از این کالا {self.product.quantity} عدد می‌باشد')
		return quantity

