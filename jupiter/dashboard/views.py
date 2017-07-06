
import os
import shutil
import requests

from django.contrib.staticfiles.storage import staticfiles_storage

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.utils import timezone
from django.utils.safestring import mark_safe
from .forms import UserLoginForm, StandardSSLCreateForm

from certificate.models import UserCertificate, UserActivateCertificate
from certificate.models import Certificate, CertificateDuration

from client.models import Message, Status

def count_days(expired_date):
    day = expired_date - timezone.now()
    return day.days


def user_status(user, message):
    status = Status.objects.create(user=user,
                status_messages=message)
    return status

@login_required(login_url="/login/")
def dashboard(request):
    active_services = UserCertificate.objects.filter(client=request.user)
    certificates = Certificate.objects.all()
    certificates_dur = CertificateDuration.objects.filter(certificate=1)
    messages = Message.objects.filter(user=request.user).order_by('-id')
    status = Status.objects.filter(user=request.user).order_by('-id')
    for service in active_services:
        if UserActivateCertificate.objects.filter(certificate=service).exists():
            activate_service = UserActivateCertificate.objects.get(certificate=service)
            service.info = activate_service.expired_date
            service.days = count_days(activate_service.expired_date)
    return render(request, "profile.html", {"active_services":active_services,
                                             "certificates":certificates,
                                             "certificates_dur":certificates_dur,
                                             "messages":messages,
                                             "status":status})


def login_view(request):
    form = UserLoginForm(request.POST or None)
    next = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "sign-in.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required(login_url="/login/")
def add_product(request):
    status = ""
    if request.method == 'POST':
        plan = request.POST['plan']
        certificates_dur = CertificateDuration.objects.get(pk=plan)
        new_certificate = UserCertificate.objects.create(client=request.user,
                    certificate=certificates_dur
        )
        status_messages = "Certificate "+str(certificates_dur)+" added in your account."
        status = user_status(request.user, status_messages)

    return HttpResponse(status)

@login_required(login_url="/login/")
def get_product(request):
    resp_ = {"status" : 404, "output" : ""}
    certificate_url = "http://localhost:1337/api/v1/get/"
    if request.method == 'GET':
        id = request.GET['id']
        url = certificate_url+id
        resp = requests.get(url).text
    return HttpResponse(resp.replace("\n", "<br>"))

@login_required(login_url="/login/")
def add_product_csr(request):
    resp = {"status" : 404, "output" : ""}
    certificate_url = "http://localhost:1337/api/v1/create/"
    if request.method == 'POST':
        csr_text = request.POST['csr_text']
        product_id = request.POST['product_id']
        duration = request.POST['duration']
        data = {'csr_text' : csr_text, 'id' : product_id, 'duration' : duration}
        resp = requests.post(certificate_url, data).json()
        # gen_cert_file = "{}_certificate_{}.crt".format(product_id, duration)
        # cert_url = staticfiles_storage.url(gen_cert_file)
        # with open(cert_url, "w") as fwrite:
        #     fwrite.write(resp["output"])

        certificates_dur = UserCertificate.objects.get(pk=product_id).certificate
        status_messages = "Certificate "+str(certificates_dur)+" is activated."
        status = user_status(request.user, status_messages)
    return HttpResponse(resp['status'])

