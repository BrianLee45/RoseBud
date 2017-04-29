from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

from . models import Event
from ..loginReg.models import User
from django.contrib import messages
from datetime import datetime, date

# Create your views here.
def index(request):
    #query, get current username, get current events & display
    context = {
        "users": User.objects.GetUser(request.session['id']),
        "today": date.today(),
        "time_list": Event.TIME_VALUES
    }
    objtrue, currentEvents = Event.objects.GetCurrentEvents()
    returnVal, futureEvents = Event.objects.GetFutureEvents()

    if objtrue:
        context.update({"events": currentEvents})
    else:
        for error in currentEvents:
            messages.error(request, error)

    if returnVal:
        context.update({"future": futureEvents})
    else:
        for error in futureEvents:
            messages.error(request, error)

    return render(request, 'odin/index.html', context)

def showUpdate(request, event_id):
    print "func showUpdate"

    isGood, objEvent = Event.objects.GetEvent(event_id)

    objEvent.eventTime = objEvent.eventTime.strftime('%H:%M')
    print type(objEvent.eventTime)

    if isGood:
        context = {
            "event": objEvent,
            "status_list": Event.STATUS_CHOICES,
            "time_list": Event.TIME_VALUES
        }
        return render(request, 'odin/update.html', context)

    else:
        for item in objEvent:
            messages.error(request, item)
        return redirect('odin:home')

def doCreateEvent(request):

    result, objEvent = Event.objects.CreateEvent(request.POST, request.session['id'])

    if result:
        return redirect('odin:home')
    else:
        for error in objEvent:
            messages.error(request, error)
        return redirect('odin:home')

    return True

def doUpdateEvent(request, event_id):

    result, objReturn = Event.objects.UpdateCurrentEvent(request.POST, event_id)

    if result:
        return redirect('odin:home')
    else:
        for error in objReturn:
            messages.error(request, error)
        return redirect('odin:showUpdate', event_id=event_id)

def doDeleteEvent(request, event_id):

    result, objReturn = Event.objects.DeleteEvent(event_id)

    if not result:
        for error in objReturn:
            messages.error(request, error)

    return redirect('odin:home')
