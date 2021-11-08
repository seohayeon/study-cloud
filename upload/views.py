from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from file.models import Category

def index(request):
    template = loader.get_template('upload/index.html')
    context = {'category':Category.objects.all()}
    return HttpResponse(template.render(context, request))
# Create your views here.

