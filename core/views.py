from django.shortcuts import render, redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username=request.POST.get('username') #recuperates parameter username from POST request on login html
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Failed to login, username or password incorrect")


    return redirect('/')

@login_required(login_url='/login/') #when not found back to login
def list_events(request):
    #event=Event.objects.all #take all, insted can use .get(id=1) or any id
    user=request.user
    event=Event.objects.filter(user=user)
    description=Event.objects.filter(user=user)
    data={'events':event, 'description': description}
    return render(request, 'agenda.html',data)

@login_required(login_url='/login/') #when not found back to login
def event(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['Event'] = Event.objects.get(id=id_evento)
    return render(request, 'event.html', dados)

@login_required(login_url='/login/') #when not found back to login
def submit_event(request):
    date_event = request.POST.get('event_date')
    description = request.POST.get('description')
    title=request.POST.get('title')
    user = request.user
    id_evento = request.POST.get('id_evento')
    if id_evento:
        event = Event.objects.get(id=id_evento)
        if event.user==user:
            event.title=title
            event.description=description
            event.date_event=date_event
            event.save()
    else:
        Event.objects.create(title=title,
                             date_event=date_event,
                             description=description,
                             user=user)
    return redirect('/')

def delete_event(request, id_evento):
    user=request.user
    event=Event.objects.get(id=id_evento)
    if user == event.user:
        event.delete()
    return redirect('/')
