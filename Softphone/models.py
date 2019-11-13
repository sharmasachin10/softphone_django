from django.db import models
from django.contrib.auth.models import User

# start TimeStamp #
class TimeStamp(models.Model):
    """Base class containing all models common information."""

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Define Model as abstract."""
        abstract = True
# end TimeStamp #


#Agents#
class Agents(TimeStamp):
    phone_number = models.CharField(max_length=20, default='', null=True)
    user_ref = models.ForeignKey(User,on_delete=models.CASCADE,default='',null=True)
    role = models.CharField(max_length=20, default='', null=True)

    def save(self, **kwargs):
        super(Agents, self).save()
    
    class Meta:
        db_table = 'agents'

#Clients#
class Clients(TimeStamp):
    client_name = models.CharField(max_length=20, default='', null=True)
    client_id = models.CharField(max_length=20, default='', null=True)
    switch_id = models.CharField(max_length=20, default='', null=True)

    def save(self, **kwargs):
        super(Clients, self).save()
    
    class Meta:
        db_table = 'clients'

#Locations#
class Locations(TimeStamp):
    compay_address = models.CharField(max_length=200, default='', null=True)
    location_type = models.CharField(max_length=20, default='', null=True)
    timezone = models.CharField(max_length=30, default='', null=True)
    client = models.ForeignKey(Clients,on_delete=models.CASCADE,default='',null=True)

    def save(self, **kwargs):
        super(Locations, self).save()
    
    class Meta:
        db_table = 'locations'

#WorkHours#
class WorkHours(TimeStamp):
    start_day = models.CharField(max_length=200, default='', null=True)
    end_day = models.CharField(max_length=20, default='', null=True)
    start_time = models.TimeField() 
    end_time = models.TimeField() 
    client = models.ForeignKey(Clients,on_delete=models.CASCADE,default='',null=True)
    location = models.ForeignKey(Locations,on_delete=models.CASCADE,default='',null=True)

    def save(self, **kwargs):
        super(WorkHours, self).save()
    
    class Meta:
        db_table = 'workhours'

#Personnel#
class Personnel(TimeStamp):
    first_name = models.CharField(max_length=50, default='', null=True)
    last_name = models.CharField(max_length=50, default='', null=True)
    email =  models.CharField(max_length=70, default='', null=True)
    phone =  models.CharField(max_length=20, default='', null=True)
    client = models.ForeignKey(Clients,on_delete=models.CASCADE,default='',null=True)
    location = models.ForeignKey(Locations,on_delete=models.CASCADE,default='',null=True)

    def save(self, **kwargs):
        super(Personnel, self).save()
    
    class Meta:
        db_table = 'personnel'

#Instructions#
class Instructions(TimeStamp):
    text =  models.CharField(max_length=1000, default='', null=True)
    client = models.ForeignKey(Clients,on_delete=models.CASCADE,default='',null=True)
    location = models.ForeignKey(Locations,on_delete=models.CASCADE,default='',null=True)

    def save(self, **kwargs):
        super(Instructions, self).save()
    
    class Meta:
        db_table = 'instructions'