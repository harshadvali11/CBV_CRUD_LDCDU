from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #queryset=School.objects.filter(Scname='Qspiders')
    #ordering=['Scname']

def wish(request,n):
    return HttpResponse(f'Hai {n} How are U')


class SchoolDetail(DetailView):
    model=School
    context_object_name='schoolobject'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'



class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobj'
    success_url=reverse_lazy('SchoolList')







