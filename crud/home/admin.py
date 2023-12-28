from django.contrib import admin
from home.models import family

class familyAdmin(admin.ModelAdmin):
    list_display=("Name","Surname")


admin.site.register(family,familyAdmin)
