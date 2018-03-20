
from django.db import models
from django.db.models.fields.files import ImageField


class Gallery(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):

        return str(self.id) + ": " + self.name

    class Meta:

        app_label = 'gallery'
        db_table = 'gallery'
        verbose_name_plural = 'Galleries'


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    caption = models.CharField(max_length=64, blank=True)
    image = ImageField(upload_to='gallery')

    def __str__(self):

        return self.gallery.name + ": " + self.image.name

    class Meta:

        app_label = 'gallery'
        db_table = 'gallery_image'
        verbose_name_plural = 'Gallery Images'
