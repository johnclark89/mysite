from django.contrib import admin
from commande.models import Pizza, Commande, CommandePizza

# Ces models sont accessibles et modifiables dans l'administration
admin.site.register(Pizza)
admin.site.register(Commande)
admin.site.register(CommandePizza)