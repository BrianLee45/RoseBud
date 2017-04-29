from __future__ import unicode_literals
from django.db import models, utils
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
        else:
            datToday = date.today()
            print datToday
            datInput = datetime.strptime(request['eventDate'], "%Y-%m-%d").date()
            if datInput < datToday:
                errors.append("Date cannot be earlier than today")

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
                if type(e) == utils.IntegrityError:
                    errors.append("You already have an appointment at that time")
                else:
                    errors.append(e.message)
                return (False, errors)
        else:
            return(False, errors)

    def UpdateCurrentEvent(self, request, data):
        print "func UpdateCurrentEvent"

        errors = []
        # data = request.get('data', data)
        strTime = request.get('eventTime', "12:00")
        print strTime
        strStatus = request.get('status', "Pending")
        #no data
        if len(request['task']) == 0:
            errors.append("Task can't be empty")

        if not EVENT_REGEX.match(request['eventDate']):
            errors.append("Please enter a valid date for the event")
        else:
            #date earlier than today
            # datToday = datetime.now().strftime('%Y-%m-%d')
            datToday = date.today()
            print datToday
            datInput = datetime.strptime(request['eventDate'], "%Y-%m-%d").date()
            if datInput < datToday:
                errors.append("Date cannot be earlier than today")

        if len(errors) == 0:
            try:
                objEvent = Event.objects.get(id=data)
                objEvent.task = request['task']
                objEvent.eventDate = request['eventDate']
                objEvent.eventTime = strTime
                objEvent.status = strStatus
                objEvent.save()
                return (True, objEvent)
            except Exception as e:
                print '%s (%s)' % (e.message, type(e))
                if type(e) == utils.IntegrityError:
                    errors.append("You already have an appointment at that time")
                else:
                    errors.append(e.message)
                return (False, errors)
        else:
            return (False, errors)


    def GetCurrentEvents(self):
        print "func GetCurrentEvents"

        errors = []

        datToday = datetime.now().strftime('%Y-%m-%d')
        objEvents = Event.objects.filter(eventDate=datToday).order_by('eventTime')
        # objEvents = Event.objects.all()

        if len(objEvents) == 0:
            errors.append("You don't have any appointments today")
            return (False, errors)
        else:
            return(True, objEvents)

    def GetFutureEvents(self):
        print "func GetFutureEvents"

        errors = []

        datLimit = datetime.now().strftime('%Y-%m-%d')
        objEvents = Event.objects.filter(eventDate__gt=datLimit)

        if len(objEvents) == 0:
            errors.append("You don't have any future appointments")
            return (False, errors)
        else:
            return (True, objEvents)

    def GetEvent(self, data):
        print "func GetEvent"
        errors = []

        try:
            objReturn = Event.objects.get(id=data)
            return (True, objReturn)
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
            errors.append(e.message)
            return (False, errors)

    def DeleteEvent(self, data):
        print "func DeleteEvent"
        errors = []

        try:
            objEvent = Event.objects.get(id=data)
            objReturn = objEvent.delete()
            return (True, objReturn)
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
            errors.append(e.message)
            return (False, errors)

        return True


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

    class Meta:
        unique_together = ('eventDate', 'eventTime')

    TIME_VALUES = (
        ("00:00", "00:00"),
        ("01:00", "01:00"),
        ("02:00", "02:00"),
        ("03:00", "03:00"),
        ("04:00", "04:00"),
        ("05:00", "05:00"),
        ("06:00", "06:00"),
        ("07:00", "07:00"),
        ("08:00", "08:00"),
        ("09:00", "09:00"),
        ("10:00", "10:00"),
        ("11:00", "11:00"),
        ("12:00", "12:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00"),
        ("17:00", "17:00"),
        ("18:00", "18:00"),
        ("19:00", "19:00"),
        ("20:00", "20:00"),
        ("21:00", "21:00"),
        ("22:00", "22:00"),
        ("23:00", "23:00")
    )
