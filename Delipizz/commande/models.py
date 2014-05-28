from django.db import models
from django.contrib.auth.models import User

'''
On va donce avoir une Commande qui contient des CommandePizza qui fait reference a Pizza
'''

# Model Pizza
class Pizza(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.CharField(max_length=500)
    def __unicode__(self):
        return self.name

# Model CommandePizza
class CommandePizza(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(Pizza)

# Model Commande
class Commande(models.Model):
    client = models.ForeignKey(User)
    date_delivery = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    commandepizza = models.ManyToManyField(CommandePizza)
    # Calcul du prix de la commande
    def get_price(self):
        calc = 0.00
        for item in self.commandepizza.all():
            calc += ( int(item.product.price)* item.quantity )
        return calc
    price = property(get_price)

