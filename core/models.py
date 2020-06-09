from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Event(models.Model): #this is a parameter
    title=models.CharField(max_length=100) #maximo de 100 caracteres
    description=models.TextField(blank=True, null=True) #can be blannk
    date_event=models.DateTimeField(verbose_name='Events date')# change the display info
    date_creation=models.DateTimeField(auto_now=True)#get now time auto
    user=models.ForeignKey(User, on_delete=models.CASCADE) #importing users from django, IF USER EXCLUDED TABLE EXCLUCED

    class Meta: #metadata
        db_table='Event' #to use your table names
    def __str__(self):
        return self.title #change object to title

    def  get_data_events(self):
        return self.date_event.strftime('%d/%m/%Y  %H:%M')
    def get_data_input_event(self):
        return self.date_event.strftime('%Y-%m-%dT%H:%M')
    def get_data_description(self):
        return self.description

    def get_late_event(self):
        if self.date_event < datetime.now():
            return True
        else:
            return False
