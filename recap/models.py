from django.db import models
from django.contrib.auth.models import User


class RecapProject(models.Model):
    name = models.CharField(max_length=30, unique=True)
    url = models.TextField(max_length=100, primary_key=True)
    description = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name


class UserProfile(models.Model):

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    participates_in = models.ManyToManyField(RecapProject, related_name='userprofile',
                                             null=True, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Participates(models.Model):
    DEV = 'DEV'
    PO = 'PO'
    ROLE_CHOICES = ((PO, 'Product Owner'), (DEV, 'Developer'), )

    role = models.CharField(max_length=3, choices=ROLE_CHOICES, default=DEV)

    user = models.ForeignKey(UserProfile)
    project = models.ForeignKey(RecapProject)


class Category(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    index = models.IntegerField();
    def __unicode__(self):
        return self.name 


class Requirement(models.Model):
    NOT_STARTED = 'NS'
    IN_PROGRESS =  'IP'
    IMPEDED = 'IM'
    DONE = 'DO'
    STATUS_CHOICES = (
        (NOT_STARTED, 'Not started'),
        (IN_PROGRESS, 'In progress'),
        (IMPEDED, 'Impeded'),
        (DONE, 'Done'),
    )
    regid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    creation_date = models.DateField();
    modified_date = models.DateField();
    priority = models.IntegerField();
    status = models.CharField(max_length=2,
                            choices=STATUS_CHOICES,
                            default=NOT_STARTED)
    belongs_to = models.ForeignKey(RecapProject, related_name='requirements')
    category = models.ForeignKey(Category, related_name='requirements_by_category') 
    responsible_person = models.ForeignKey(User, related_name='my_requirements', 
                                           null=True, blank=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.regid
    

