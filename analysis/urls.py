from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('company/<int:pk>', views.CompanyView.as_view(), name='company'),
    path('statement_detail/<int:pk>', views.StatementView.as_view(), name='statement'),
]