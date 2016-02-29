from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils.html import format_html
import os

def map_file_name(instance, filename):
    return 'map_images/' + os.urandom(6).encode('hex') + '_' +filename

def calib_image_name(instance, filename):
    return 'calib_images/' + os.urandom(6).encode('hex') + '_' + filename


class Map(models.Model):
    description = models.CharField('Description', max_length=2000)
    floor = models.IntegerField('Floor', default=0)
    image = models.ImageField('Map Image', upload_to=map_file_name, height_field='im_height', width_field='im_width')
    def image_url(self):
        return format_html(u'<img style="width: 400px; height: auto;" src="/%s/%s">' % (settings.MEDIA_URL, self.image))
    im_height = models.PositiveIntegerField('Height', editable=False)
    im_width = models.PositiveIntegerField('Width', editable=False)
    date_added = models.DateTimeField('Date Added', auto_now_add=True)
    date_modified = models.DateTimeField('Date Modified', auto_now=True)
    scale = models.FloatField('Scale px to m')

class Calibration(models.Model):
    image = models.ImageField('Map Image', upload_to=calib_image_name, height_field='im_height', width_field='im_width')
    im_height = models.PositiveIntegerField('Height')
    im_width = models.PositiveIntegerField('Width')


class Camera(models.Model):
    location = models.CharField('Location', max_length=1000)
    date_added = models.DateTimeField('Date Added', auto_now_add=True)
    date_modified = models.DateTimeField('Date Modified', auto_now=True)
    gps_la = models.DecimalField('Latitude', max_digits=9, decimal_places=6)
    gps_lo = models.DecimalField('Longitude', max_digits=9, decimal_places=6)
    height = models.PositiveIntegerField('Height')
    map_id = models.ForeignKey(Map,  null=True, blank=False, on_delete=models.SET_NULL)


