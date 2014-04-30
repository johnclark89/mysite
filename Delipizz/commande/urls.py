from django.conf.urls import patterns, url

from commande import views


urlpatterns = patterns('',
    	url(r'^$', views.index, name='index'),
    	#url(r'^reservation$', views.reservation, name='reservation')
        url(r'^accueil$', views.accueil, name='accueil'),
        url(r'^infos', views.infos, name='infos'),
        url(r'^commande$', views.commande, name='commande$'),
        url(r'^about', views.about, name='apropos'),
)