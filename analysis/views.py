from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, DetailView
from .models import Company, Statement
from django.views.generic.list import MultipleObjectMixin 

class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        company_list = Company.objects.all().order_by('id')
        params = {'company_list': company_list,}
        return params

class CompanyView(DetailView, MultipleObjectMixin):
    model = Company
    paginate_by = 4

    def get_context_data(self, **kwargs):
        object_list = Statement.objects.filter(company=kwargs['object']).order_by('-fiscal_year')
        context = super(CompanyView, self).get_context_data(object_list=object_list, **kwargs)
        return context

class StatementView(DetailView):
    model = Statement