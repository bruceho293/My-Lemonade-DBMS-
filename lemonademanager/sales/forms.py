from django import forms
from django.core.exceptions import ValidationError

from .models import Sale, Staff
from datetime import datetime

class SalesForm(forms.ModelForm):
    # error_css_class = "error"

    class Meta:
        model = Sale
        fields = ['staff_id', 'product_id', 'quantity']
        labels = {
            'staff_id': "Staff",
            'product_id': "Product",
        }

    def clean(self):
        cleaned_data = super(SalesForm, self).clean()
        if cleaned_data.get('quantity') <= 0:
            self.fields['quantity'].widget.attrs['class'] = "error"
            raise ValidationError("Cannot submit a Sale with no items")

class ReportForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': "YYYY-MM-DD"}))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'placeholder': "YYYY-MM-DD"}))

    class Meta:
        model = Sale
        fields = ['staff_id', 'start_date', 'end_date']
        labels = {
            'staff_id': "Staff\'s Name and ID"
        }

    def clean(self):
        cleaned_data = super(ReportForm, self).clean()
        if cleaned_data.get('start_date') > cleaned_data.get('end_date'):
            raise ValidationError("Impossible date range.")

class SecondSalesForm(forms.Form):
    staff_id = forms.DecimalField(max_digits=9, decimal_places=0);
    product = forms.CharField(max_length=30);
    quantity = forms.IntegerField();
