from django.contrib import admin
from .models import FinancialUpdate, Notification

admin.site.register(FinancialUpdate)
admin.site.register(Notification)