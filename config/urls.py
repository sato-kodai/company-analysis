from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from .settings import base, local

urlpatterns = [
    path('', include('analysis.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(local.STATIC_URL, 
document_root=local.STATIC_ROOT)