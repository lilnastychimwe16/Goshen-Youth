from django.shortcuts import render, redirect
from .forms import FinancialUpdateForm, NotificationForm
from .models import FinancialUpdate, Notification

def index(request):
      # financial_updates = FinancialUpdate.objects.all()
   # notifications = Notification.objects.all()
    return render(request, 'index.html')# {
      #  'financial_updates': financial_updates,
        #'notifications': notifications,
    #})
    financial_updates = FinancialUpdate.objects.all()
    notifications = Notification.objects.all()
    return render(request, 'youth/index.html', {
        'financial_updates': financial_updates,
        'notifications': notifications,
    })

def add_financial_update(request):
    if request.method == 'POST':
        form = FinancialUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FinancialUpdateForm()
    return render(request, 'youth/add_financial_update.html', {'form': form})

def add_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NotificationForm()
    return render(request, 'youth/add_notification.html', {'form': form})