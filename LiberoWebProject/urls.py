"""
Definition of urls for LiberoWebProject.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path("pelanggan/", views.PelangganListView.as_view(), name='pelanggan_list'),
    path("penawaran/", views.PenawaranListView.as_view(), name='penawaran_list'),
    path("penawaran/add", views.PenawaranCreateView, name='penawaran_form')
]