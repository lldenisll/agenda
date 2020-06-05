from django.shortcuts import render
from core.models import Event

# Create your views here.

def list_events(request):
    event=Event.objects.all #take all, insted can use .get(id=1) or any id
    #user=request.user
    #event=Event.objects.filter(user=user)
    data={'events':event}
    return render(request, 'agenda.html',data)