from django.contrib import admin
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api-auth/', include('djangorestframework.urls', namespace='djangorestframework')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('readings.urls')),
)
