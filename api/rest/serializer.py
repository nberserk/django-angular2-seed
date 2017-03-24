from __future__ import unicode_literals


from rest_framework import serializers

from rest.models import People


class PeopleSerializer(serializers.ModelSerializer)
    class Meta:
        model = People
