from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from . import settings_local

urlpatterns = [
    path('', include('analysis.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings_local.STATIC_URL, document_root=settings_local.STATIC_ROOT)
urlpatterns += static(settings_local.MEDIA_URL, document_root=settings_local.MEDIA_ROOT)