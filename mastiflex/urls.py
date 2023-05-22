from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mastiflex_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),

]