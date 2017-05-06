from django.contrib import admin

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

       
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'messages', 'read_status', 'date', 'status')
admin.site.register(Message, MessageAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status_messages', 'read_status', 'date', 'status')
admin.site.register(Status, StatusAdmin)

