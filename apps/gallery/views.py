from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Gallery


class GalleryView(TemplateView):

    template_name = 'gallery.html'

    def get(self, request):

        galleries = Gallery.objects.prefetch_related('galleryimage_set').all()

        return render(request, self.template_name, {'galleries': galleries})
