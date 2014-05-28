from django.conf.urls import patterns, url
from commande import views


urlpatterns = patterns('',

    # General urls
    url(r'^accueil$', views.accueil, name='accueil'),
    url(r'^infos', views.infos, name='infos'),
    url(r'^pizzas', views.pizzas, name='pizzas'),
    url(r'^commande$', views.commande, name='commande'),
    url(r'^about', views.about, name='apropos'),

    # Registration urls
    url(r'accounts/register/$', views.register_user, name='register_user'),
    url(r'accounts/register_success/$', views.register_success, name='register_succes'),

    # User auth urls
    url(r'accounts/auth/$', views.auth_view, name='auth_view'),
    url(r'accounts/logout/$', views.logout, name='logout'),
    url(r'accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'accounts/invalid/$', views.invalid_login, name= 'invalid_login'),

)