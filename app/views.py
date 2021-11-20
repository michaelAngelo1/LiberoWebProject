"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

from django.views import generic
from django.db import models
from .models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from app.forms import PenawaranForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

class PelangganListView(generic.ListView):
    model = Pelanggan

class PenawaranListView(generic.ListView):
    model = Penawaran
    template_name = 'app/penawaran_list.html'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'CreateBy', None) is None:
            obj.CreateBy = request.user.username
            obj.Operator = request.user.username
        elif getattr(obj, 'Operator', None) != request.user.username:
            obj.Operator = request.user.username
        obj.save()

def PenawaranCreateView(request):
    if request.method=='POST':
          form = PenawaranForm(request.POST)
          if form.is_valid():
              penawaran = PenawaranModel()
              penawaran.CreateBy = form.cleaned_data['CreateBy']
              penawaran.Operator = form.cleaned_data['Operator']
              penawaran.save()
              return redirect('penawaran_list')
          else:
              initial = {'CreateBy':request.user.username}
              form = PenawaranForm(initial=intial)
    else:
        form = PenawaranForm()
    return render(request, 'penawaran_form.html')


