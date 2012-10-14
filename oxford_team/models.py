from django.db import models

from django_extensions.db.fields import CreationDateTimeField


class Team(models.Model):
    user = models.OneToOneField('auth.User')
    name = models.CharField(max_length=255)
    created = CreationDateTimeField()
    bowstyle = models.CharField(max_length=15, choices=(('Recurve', 'Recurve'), ('Compound', 'Compound')))
    paid = models.BooleanField()
    paid_amount = models.IntegerField(blank=True, null=True)
    paid_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Archer(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey('Team')
    fb_id = models.CharField(max_length=100, blank=True, null=True)
    gnas_no = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name
