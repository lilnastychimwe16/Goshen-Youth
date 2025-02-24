from django.shortcuts import render
from .models import FinancialUpdate, Notification

def index(request):
    financial_updates = FinancialUpdate.objects.all()
    notifications = Notification.objects.all()
    return render(request, 'youth/index.html', {
        'financial_updates': financial_updates,
        'notifications': notifications,
    })