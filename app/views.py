from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView
from django.http import HttpResponse

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











