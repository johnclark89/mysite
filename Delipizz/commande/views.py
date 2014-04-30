# Create your views here.
from django.shortcuts import render


def index(request):
    #code

    return render(
        request,
        "index.html",
    )

def accueil(request):
    return render(
        request,
        "accueil.html",
    )

def infos(request):
    return render(
        request,
        "infos.html",
    )
def commande(request):
    return render(
        request,
        "commande.html",
    )
def about(request):
    return render(
        request,
        "about.html",
    )


	