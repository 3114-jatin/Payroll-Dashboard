from django.contrib import admin
from .models import Employee, Attendance, IncomeTax

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(IncomeTax)
