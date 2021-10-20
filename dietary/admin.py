from django.contrib import admin
from .models import DietaryItem


class DietaryItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(DietaryItem, DietaryItemAdmin)
