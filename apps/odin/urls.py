from django.conf.urls import url
from . import views

app_name = "odin"

urlpatterns = [
    url(r'^$', views.index, name='home'),
    # url(r'^showCreate$', views.showCreate, name='showCreate'),
    url(r'^create$', views.doCreateEvent, name='create'),
    url(r'^showUpdate$', views.showUpdate, name='showUpdate'),
]
