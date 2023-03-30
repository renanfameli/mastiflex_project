from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mastiflex_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]




