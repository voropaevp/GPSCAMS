from django.contrib import admin
from django.conf import settings
from .models import Camera, Map
from django.template.loader import get_template, render_to_string
from PIL import Image
import os

# Register your models here.


class MapDisplay(admin.ModelAdmin):
    list_display = ['image_url', 'description', 'scale']
    ordering = ['date_added']
    actions = ['render_map']

    def render_map(self, request, queryset):
        path = settings.MEDIA_ROOT + '\\\\' + queryset.first().image.name
        im = Image.open(path)
        tmpl = get_template('map.xml')
        pre, _ = os.path.splitext(path)
        im.save(pre + ".tiff", "TIFF")
        f = open(pre + '.xml', 'w')
        f.write(tmpl.render({'filename': (pre + ".tiff")}))
        f.close()
    render_map.short_description = 'Render image to map tiles'

admin.site.register(Camera)
admin.site.register(Map, MapDisplay)