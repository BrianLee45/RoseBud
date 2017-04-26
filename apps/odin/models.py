from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date
from ..loginReg.models import User
import re

# EVENT_REGEX = re.compile(r'^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d$')
EVENT_REGEX = re.compile(r'^\b\d{4}[-/:]\d{1,2}[-/:]\d{1,2}\b$')


class EventManager(models.Manager):
    def CreateEvent(self, request, user_id):
        print "func CreateEvent"
        errors = []
        strTime = request.get('eventTime', "12:00")

        #pull values from selectors
        if len(request['task']) == 0:
            errors.append("Task cannot be empty")
        # eventDate
        if not EVENT_REGEX.match(request['eventDate']):
            errors.append("Please enter a valid date for the event")

        objUser = User.objects.GetUser(user_id)[0]
        print objUser
        print request['task']
        print request['eventDate']
        print strTime

        if len(errors) == 0:
            try:
                objReturn = Event.objects.create(
                    creator = objUser,
                    task = request['task'],
                    eventDate = request['eventDate'],
                    eventTime = strTime
                    # eventDate = datetime.strptime(request['eventDate'], "%m/%d/%Y").date(),
                    # eventTime = datetime.strptime(strTime, "%H:%M").date()
                )
                return (True, objReturn)
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
                errors.append(e.message)
                return (False, errors)
        else:
            return(False, errors)

    def GetCurrentEvents(self):
        print "func GetCurrentEvents"

        errors = []

        # now = datetime.datetime.now()

        datToday = datetime.now()
        datToday.strftime('%Y-%m-%d')
        objEvents = Event.objects.filter(eventDate=datToday)

        if len(objEvents) == 0:
            errors.append("You don't have any appointments today")
            return (False, errors)
        else:
            return(True, objEvents)


# Create your models here.
class Event(models.Model):
    DONE = "Done"
    MISSED = "Missed"
    PENDING = "Pending"
    STATUS_CHOICES = (
        (DONE, "Done"),
        (MISSED, "Missed"),
        (PENDING, "Pending")
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    task = models.CharField(max_length=140)
    eventDate = models.DateField(default=date.today)
    eventTime = models.TimeField(default=date.today)
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    objects = EventManager()
