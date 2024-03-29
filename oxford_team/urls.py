from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social/', include('socialregistration.urls', namespace='socialregistration')),
)

urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
