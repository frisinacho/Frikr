from django.contrib import admin

# Register your models here.
from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner', 'license', 'visibility')


admin.site.register(Photo, PhotoAdmin)
