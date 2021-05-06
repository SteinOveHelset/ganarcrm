from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import viewsets

from team.models import Team

from .models import Client
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        serializer.save(team=team, created_by=self.request.user)

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        return self.queryset.filter(team=team)