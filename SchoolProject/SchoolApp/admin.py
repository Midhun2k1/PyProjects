from django.contrib import admin

# Register your models here.
from .models import Department, Course, FormSubmission, Material


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']


admin.site.register(Department, DepartmentAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Course, CourseAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Material, MaterialAdmin)


class FormAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'purpose']


admin.site.register(FormSubmission, FormAdmin)
