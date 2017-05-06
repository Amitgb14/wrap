from __future__ import unicode_literals

from django.contrib.auth.models import User 
from django.db import models
from django.utils import timezone

STATUS_CHOICES = ((1, 'Yes'),(0, 'No'),)

class ClientInfo(models.Model):
    user = models.OneToOneField(User, null=True, related_name="user_info")
    first_name = models.CharField("First Name", max_length=200, blank=False)
    last_name = models.CharField("Last Name", max_length=200, blank=False)
    email_id = models.EmailField("Email id", blank=False, unique=True)
    contact_no = models.CharField("Contact Numer", max_length=15, blank=True, unique=True)
    status = models.BooleanField('Status', default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Message(models.Model):
    user = models.ForeignKey(User, null=True, related_name="user_messages")
    messages = models.TextField("Messages")
    read_status = models.BooleanField('Read_Status', default=1, choices=STATUS_CHOICES, blank=False)
    date = models.DateTimeField("Date", default=timezone.now, blank=False)
    status = models.BooleanField('Status', default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "{}".format(self.user)

class Status(models.Model):
    user = models.ForeignKey(User, null=True, related_name="user_status")
    status_messages = models.TextField("Status")
    read_status = models.BooleanField('Read_Status', default=1, choices=STATUS_CHOICES, blank=False)
    date = models.DateTimeField("Date", default=timezone.now, blank=False)
    status = models.BooleanField('Status', default=1, choices=STATUS_CHOICES, blank=False)
    def __str__(self):
        return "{}".format(self.user)
    
    
