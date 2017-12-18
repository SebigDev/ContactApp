from django.contrib import admin
from .models import StaffManager, Manager, ActiveManager

# Register your models here.

admin.site.register(Manager)
admin.site.register(StaffManager)
admin.site.register(ActiveManager)


