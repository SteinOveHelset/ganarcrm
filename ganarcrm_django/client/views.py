from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from lead.models import Lead
from team.models import Team

from .models import Client, Note
from .serializers import ClientSerializer, NoteSerializer

class ClientPagination(PageNumberPagination):
    page_size = 10

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'contact_person')
    
    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        serializer.save(team=team, created_by=self.request.user)

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()

        return self.queryset.filter(team=team)

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.GET.get('client_id')

        return self.queryset.filter(team=team).filter(client_id=client_id)

    def perform_create(self, serializer):
        team = Team.objects.filter(members__in=[self.request.user]).first()
        client_id = self.request.data['client_id']

        serializer.save(team=team, created_by=self.request.user, client_id=client_id)

@api_view(['POST'])
def convert_lead_to_client(request):
    team = Team.objects.filter(members__in=[request.user]).first()
    lead_id = request.data['lead_id']

    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
    except Lead.DoesNotExist:
        raise Http404
    
    client = Client.objects.create(team=team, name=lead.company, contact_person=lead.contact_person, email=lead.email, phone=lead.phone, website=lead.website, created_by=request.user)

    return Response()

@api_view(['POST'])
def delete_client(request, client_id):
    team = Team.objects.filter(members__in=[request.user]).first()

    client = team.clients.filter(pk=client_id)
    client.delete()

    return Response({'message': 'The client was deleted'})