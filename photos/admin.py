from django.contrib import admin

# Register your models here.
from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner_name', 'license', 'visibility')
    list_filter = ('license', 'visibility')
    search_fields = ('name', 'description')

    def owner_name(self, obj):
        return obj.owner.first_name + u' ' + obj.owner.last_name
    owner_name.short_description = u'Photo owner'
    owner_name.admin_order_field = 'owner'

    fieldsets = (
        (None, {
            'fields': ('name',),
            'clases': ('wide',),
        }),
    )

admin.site.register(Photo, PhotoAdmin)
