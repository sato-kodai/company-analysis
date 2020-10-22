from django.contrib import admin
from django.urls import path, include
from accounts.views import Top

urlpatterns = [
    path('', Top.as_view(), name='top'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

