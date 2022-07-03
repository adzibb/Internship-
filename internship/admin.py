from django.contrib import admin
from .models import Company, Location, CompanyRole, Student

# Register your models here.

admin.site.register(CompanyRole)
admin.site.register(Company)
admin.site.register(Location)
admin.site.register(Student)