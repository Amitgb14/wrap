from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from certificate.models import Certificate, CertificateDuration
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Fieldset, ButtonHolder, Submit

User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class StandardSSLCreateForm(forms.Form):
    CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)
    d = CertificateDuration.objects.all()
    certificate_  = forms.ModelChoiceField(queryset=d, widget=forms.RadioSelect, empty_label=None)
    csr_text = forms.CharField(required=True, widget=forms.Textarea)
