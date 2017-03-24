from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from rest.models import People
from rest.serializer import PeopleSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = PeopleSerializer
    queryset = People.objects.all()

