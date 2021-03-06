from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Delipizz.views.home', name='home'),
    # url(r'^Delipizz/', include('Delipizz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Ajout des urls propres a l'application
    url(r'delipizz/', include('commande.urls')),

    # Ajout des urls de Foundation
    url(r'foundation/', include('foundation.urls')),
)
