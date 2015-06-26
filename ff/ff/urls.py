from django.conf.urls import include, url, patterns


from django.contrib import admin
from item.views import *

# from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rules/$', rules),
    url(r'^forgotpass/$', forgotpass),
    url(r'^nocode/$', nocode),
    url(r'^about/$', about),
    url(r'^signup/$', signup),
    url(r'^$', index),
    ]

# if settings.DEBUG:
# 	urlpatterns += static(settings.STATIC_URL,
# 		document_root=settings.STATIC_ROOT)
# 	urlpatterns += static(settings.MEDIA_URL,
# 		document_root=settings.MEDIA_ROOT)