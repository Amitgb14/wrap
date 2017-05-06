from __future__ import unicode_literals
from django.contrib.auth.models import User 
from django.db import models
from django.utils import timezone

import uuid

STATUS_CHOICES = ((1, 'Yes'),(0, 'No'),)

INTERMEDIATE_CERTIFICATE = (
   ('W1', 'Wrapdigi Authority W1'),
   ('W2', 'Wrapdigi Authority W2'),
)
 
def get_random_uuid(length=5):
    """Returns random string"""
    random = str(uuid.uuid4()).upper().replace("-","")
    return random[:length]


class Certificate(models.Model):
    certificate_name = models.CharField("Certificate Name", max_length=200, default="Standard SSL", blank=False)
    status = models.BooleanField('Status', default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return self.certificate_name


class CertificateDuration(models.Model):
    certificate = models.ForeignKey(Certificate)
    duration = models.IntegerField('Duration (Years)', default=1, blank=False)
    cost = models.IntegerField('Cost', default=20, blank=False)
    status = models.BooleanField('Status', default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "{0} - ({1} Year)".format(self.certificate, self.duration)


class UserCertificate(models.Model):
    client = models.ForeignKey(User)
    certificate_number = models.CharField('Certificate Number', max_length=20, default=get_random_uuid, blank=False)
    certificate = models.ForeignKey(CertificateDuration)
    created_date = models.DateTimeField("Created Date", default=timezone.now, blank=False)
    activate = models.BooleanField('Activate', default=0, choices=STATUS_CHOICES, blank=False)
    status = models.BooleanField('Status', default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "{}-{}".format(self.certificate_number, self.certificate)


class UserActivateCertificate(models.Model):
    certificate = models.ForeignKey(UserCertificate)
    certificate_text = models.TextField("Certificate", blank=False)
    issued_by = models.CharField("Issued By", default=1, max_length=20, choices=INTERMEDIATE_CERTIFICATE, blank=False)
    issued_date = models.DateTimeField("Issued Date", default=timezone.now, blank=False)
    expired_date = models.DateTimeField("Expired Date", blank=False)
    status = models.BooleanField('Status', default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "Certificate {} activated".format(self.certificate)


