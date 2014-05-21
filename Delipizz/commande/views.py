# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm


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

# auth views
def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/delipizz/accounts/register_success')
        else:
            print 'form invalid'

    args = {}
    args.update(csrf(request))

    args['form'] = MyRegistrationForm()

    return render_to_response('register.html', args)



def register_success(request):
    return render_to_response('register_success.html')




def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/delipizz/accounts/loggedin')
    else:
        return HttpResponseRedirect('/delipizz/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')