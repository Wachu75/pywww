from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail
from galleries.models import Gallery
from galleries.models import Photo


class GalleryResource(resources.ModelResource):
    class Meta:
        model = Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'description', 'created', 'modified', 'status']


class PhotoResource(resources.ModelResource):
    class Meta:
        model = Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'image', 'gallery', 'created', 'modified', 'source', 'status',]


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            t = get_thumbnail(value, "150")
            output.append(f'<a href="{value.url}" target="_blank"><img src="{t.url}"></a>')
        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        # return mark_safe(''.join(output))
        return ''.join(output)