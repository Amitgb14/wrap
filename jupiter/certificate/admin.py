from django.contrib import admin
from datetime import datetime, timedelta
from django.utils import timezone

from .models import *

def mark_enable(obj, request, queryset):
        rows_update=queryset.update(status=1)
        mm(obj,rows_update, request,"Enable")
def mark_disable(obj, request, queryset):
        rows_update=queryset.update(status=0)
        mm(obj,rows_update, request,"Disable")
mark_enable.short_description="Enable"
mark_disable.short_description="Disable"

def mm(obj,rows_update, request, work):
       if rows_update==1:
          msg="1 story was"
       else:
          msg="%s stories were" % rows_update
       obj.message_user(request,"%s successfully as %s." % (msg, work))


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'certificate_name', 'status')
admin.site.register(Certificate, CertificateAdmin)


class CertificateDurationAdmin(admin.ModelAdmin):
    list_display = ('id', 'certificate', 'duration', 'cost', 'status')
admin.site.register(CertificateDuration, CertificateDurationAdmin)


class UserCertificateAdmin(admin.ModelAdmin):
  list_display = ('id', 'client', 'certificate_number', 'certificate', 'created_date', 'activate', 'status')
  list_filter  = ('client', 'certificate',)
  actions = [mark_enable, mark_disable]
  order = ['id']
admin.site.register(UserCertificate, UserCertificateAdmin)


class UserActivateCertificateAdmin(admin.ModelAdmin):
  list_display = ('id', 'certificate', 'certificate_text', 'issued_by', 'issued_date', 'expired_date', 'remaining_days', 'status')
  actions = [mark_enable, mark_disable]
  order = ['id']

  def certificata(self, obj):
      return '<a href="{0}">{1}</a>'.format(obj.certificate.url, obj.certificate)
  certificata.allow_tags = True

  def remaining_days(self, obj):
      now = timezone.now()
      day = obj.expired_date - now
      return day.days
admin.site.register(UserActivateCertificate, UserActivateCertificateAdmin)
