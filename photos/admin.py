from django.contrib import admin

# Register your models here.
from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner', 'license', 'visibility')
    list_filter = ('license', 'visibility')
    search_fields = ('name', 'description')


admin.site.register(Photo, PhotoAdmin)
