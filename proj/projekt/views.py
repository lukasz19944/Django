from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from projekt.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render_to_response, render, get_object_or_404
from projekt.models import *


def main_page(request):
    wizytowki = Wizytowka.objects.all()
    return render(request, 'main_page.html', {'wizytowki': wizytowki})
    
@csrf_exempt 
def card_create(request):
    if request.method == 'POST':
        form = FormularzWizytowka(request.POST)
        if form.is_valid():
            user = request.user
            wizytowka = Wizytowka()
            wizytowka.utworz(
                imie = user.first_name,
                nazwisko = user.last_name,
                uczelnia = form.cleaned_data['uczelnia'],
                kierunek = form.cleaned_data['kierunek'],
                telefon = form.cleaned_data['telefon'],
                email = user.email,
            )
            
            wizytowka.save()
            
            template = get_template("creating_success.html")
            variables = RequestContext(request,{'user':user})
            output = template.render(variables)
            return HttpResponse(output) 
            
    else:
        form = FormularzWizytowka()
            
    template = get_template("card_create.html")    
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)
    
@csrf_exempt 
def register_page(request):
    if request.method == 'POST':
        form = FormularzRejestracji(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
              username=form.cleaned_data['username'],
              password=form.cleaned_data['password1'],
              email=form.cleaned_data['email'],
              first_name=form.cleaned_data['first_name'],
              last_name=form.cleaned_data['last_name'],
            )
            user.save()
            if form.cleaned_data['log_on']:
                user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
                login(request,user)
                template = get_template("main_page.html")
                variables = RequestContext(request,{'user':user})
                output = template.render(variables)
                return HttpResponseRedirect("/") 
            else:    
                template = get_template("registration/register_success.html")
                variables = RequestContext(request,{'username':form.cleaned_data['username']})
                output = template.render(variables)
                return HttpResponse(output)            
    else:
        form = FormularzRejestracji()
    template = get_template("registration/register.html")    
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)
    
@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        form = FormularzLogowania(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            login(request,user)
            template = get_template("main_page.html")
            variables = RequestContext(request,{'user':user})
            output = template.render(variables)
            return HttpResponseRedirect("/")           
  
    else: 
        form = FormularzLogowania()
    template = get_template("registration/login.html")    
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/")