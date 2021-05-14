from django.contrib.auth.models import User
from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=255)
    max_leads = models.IntegerField(default=5)
    max_clients = models.IntegerField(default=5)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    plan = models.ForeignKey(Plan, related_name='teams', on_delete=models.SET_NULL, null=True, blank=True)