from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse
from app.forms import *
# Create your views here.
class datainsert_bytv(TemplateView):
    template_name='datainsert_bytv.html'

    def get_context_data(self, **kwargs):
        ECDO= super().get_context_data(**kwargs)
        #ECDO['name']='Amuliya'
        #ECDO['age']=21
        ECDO['ECDO']=CollegeForm()
        return ECDO
    
    #FORM VIEW

    def post(self,request):
        CFDO=CollegeForm(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('datainsert_bytv is done')
        else:
            return HttpResponse('datainsert_bytv not done')
        
class InsertDaataByFv(FormView):
    template_name='InsertDaataByFv.html'
    form_class=CollegeForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('formview is done successfully')
       