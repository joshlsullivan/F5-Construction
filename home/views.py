from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

class HomeView(TemplateView):
    template_name = "home/index.html"
