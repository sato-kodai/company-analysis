from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Statement


class Top(generic.TemplateView):
    template_name = 'top.html'

    def get_context_data(self, **kwargs):
      statement_list = Statement.objects.all().order_by('company')
      params = {'statement_list': statement_list,}
      return params