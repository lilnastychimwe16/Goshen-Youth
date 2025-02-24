from django.contrib import admin
from django.urls import include, path
from youth import views  # Import views directly if needed

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', views.index, name='index'),  # Root URL mapped to index view of youth app
    # If you have more URLs in youth app, include them like below
    path('youth/', include('youth.urls')),  # Include all youth app URLs
]