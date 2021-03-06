from django import forms
from django.core.exceptions import ValidationError

from .models import Sale, Staff
from datetime import datetime

class SalesForm(forms.ModelForm):
    # error_css_class = "error"

    class Meta:
        model = Sale
        fields = ['staff', 'product', 'quantity']
        labels = {
            'staff': "Staff",
            'product': "Product",
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
        fields = ['staff', 'start_date', 'end_date']
        labels = {
            'staff': "Staff\'s Name and ID"
        }

    def clean(self):
        cleaned_data = super(ReportForm, self).clean()
        if cleaned_data.get('start_date') > cleaned_data.get('end_date'):
            raise ValidationError("Impossible date range.")
