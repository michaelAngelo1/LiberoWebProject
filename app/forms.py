"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import *
from django.forms import ModelForm

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class PenawaranForm(ModelForm):
    class Meta:
        model = Penawaran
        fields = ['Tanggal', 'pelanggan', 'AlamatTreatment', 'JenisPekerjaan', 'Metode', 'Harga', 'Keterangan', 'Sales', 'TanggalPeriode', 'Status', 'NoPenawaran', 'HargaDeal', 'TglDeal', 'Sumber', 'ReferralLead']

