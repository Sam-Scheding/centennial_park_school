"""centennial_park_school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from apps.gallery import views as gallery_views
from apps.contact import views as contact_views
from apps.staff import views as staff_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls')), 
    url(r'', include('apps.main.urls')),
    # url(r'^gallery/', gallery_views.GalleryView.as_view()),
    url(r'^contact/', contact_views.ContactView.as_view()),
    url(r'^staff/', staff_views.StaffView.as_view()),
    url(r'^console/', include('apps.console.urls')),
    url(r'^tracking/behaviour/', include('apps.behaviour.urls')),
    # url(r'^tracking/wios', include('apps.wios.urls')),
    url(r'^downloads/', include('apps.downloads.urls')),
    url(r'^api/', include('apps.api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
