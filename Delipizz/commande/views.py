from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm, CommandeForm, CommandePizzaForm
from django.forms.formsets import formset_factory, BaseFormSet
from commande.models import Pizza, Commande, CommandePizza
from django.template import RequestContext


'''
General
'''
# Vue commande
def commande(request):
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False
    TodoItemFormSet = formset_factory(CommandePizzaForm, max_num=10, formset=RequiredFormSet)
    if request.method == 'POST': # If the form has been submitted...
        todo_list_form = CommandeForm(request.POST) # A form bound to the POST data
        # Create a formset from the submitted data
        todo_item_formset = TodoItemFormSet(request.POST, request.FILES)
        if todo_list_form.is_valid() and todo_item_formset.is_valid():
            todo_list = todo_list_form.save()
            for form in todo_item_formset.forms:
                todo_item = form.save(commit=False)
                todo_item.list = todo_list
                todo_item.save()
            return HttpResponseRedirect('thanks') # Redirect to a 'success' page
        else:
            print 'error'
    else:
        todo_list_form = CommandeForm()
        todo_item_formset = TodoItemFormSet()
    # For CSRF protection
    # See http://docs.djangoproject.com/en/dev/ref/contrib/csrf/
    c = {'todo_list_form': todo_list_form,
         'todo_item_formset': todo_item_formset,
        }
    c.update(csrf(request))
    return render_to_response('commande.html', c)

# Vue pizzas
def pizzas(request):
    c = {'pizzas': Pizza.objects.all()}
    c.update(csrf(request))
    return render_to_response('liste.html', c)

# Vue accueil
def accueil(request):
    return render(
        request,
        "accueil.html",
    )

# Vue infos
def infos(request):
    return render(
        request,
        "infos.html",
    )

# Vue A propos
def about(request):
    return render(
        request,
        "about.html",
    )


'''
Compte
'''
# Vue creation d'utilisateur
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

# Vue enregistrement reussi
def register_success(request):
    return render_to_response('register_success.html')

# Vue auth
def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/delipizz/accounts/loggedin')
    else:
        return HttpResponseRedirect('/delipizz/accounts/invalid')

# Vue connection reussie
def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

# Vue connection non reussie
def invalid_login(request):
    return render_to_response('invalid_login.html')

# Vue deconnection
def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

