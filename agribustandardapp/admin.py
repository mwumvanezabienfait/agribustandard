from django.contrib import admin
from .models import Crop
# Register your models here.


# class CropAdmin(admin.ModelAdmin):
#     pass
#
#
# admin.site.register(Crop)


class CropAdmin (admin.ModelAdmin):
    list_display =['phoneNumber', 'names']
    search_fields =['phoneNumber']


admin.site.register(Crop, CropAdmin)