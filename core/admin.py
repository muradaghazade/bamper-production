from django.contrib import admin
from core.models import *
from django.contrib.auth.models import Group
admin.site.register(Order)
admin.site.register(Store)
admin.site.register(Contact)
admin.site.unregister(Group)
