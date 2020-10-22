from django.urls import path

from . import views

app_name = 'analysis'

urlpatterns = [
    path('', views.TopView.as_view(), name='Top'),
]