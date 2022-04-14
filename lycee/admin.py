from django.contrib import admin

# Register your models here.
from .models import Student, Cursus

class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")


class CursusAdmin(admin.ModelAdmin):
    fieldsets = [
        ('zone1', {'fields': ["name"]}),
        ('zone2', {'fields': ["scholar_year", "year_from_bac"], 'classes': ['collapse']})
    ]

admin.site.register(Student,StudentAdmin)
admin.site.register(Cursus,CursusAdmin)