from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from rest.models import People


class PeopleViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = People.objects.all()

