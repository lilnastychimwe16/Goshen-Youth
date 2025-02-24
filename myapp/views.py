from django.shortcuts import render
from .models import MyModel

def index(request):
    items = MyModel.objects.all()
    return render(request, 'myapp/index.html', {'items': items})
