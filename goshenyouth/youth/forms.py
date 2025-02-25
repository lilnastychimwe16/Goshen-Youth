from django import forms
from .models import FinancialUpdate, Notification

class FinancialUpdateForm(forms.ModelForm):
    class Meta:
        model = FinancialUpdate
        fields = ['title', 'amount', 'description']

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['title', 'message']