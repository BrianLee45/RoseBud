from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

from . models import Event
from ..loginReg.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    #query, get current username, get current events & display
    context = {
        "users": User.objects.GetUser(request.session['id']),
        "events": Event.objects.GetCurrentEvents()
    }
    # objReturn = User.objects.GetUser(request.session['id'])
    # print objReturn.first_name

    return render(request, 'odin/index.html', context)

def showUpdate(request):

    return render(request, 'odin/update.html')

def doCreateEvent(request):

    result, objEvent = Event.objects.CreateEvent(request.POST, request.session['id'])

    if result:
        return redirect('odin:home')
    else:
        for error in objEvent:
            messages.error(request, error)
        return redirect('odin:home')

    return True

def doUpdateEvent(request):

    pass
    return True
