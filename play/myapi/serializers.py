from rest_framework import serializers

from play.myapi.models import Hero


class HeroSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Hero
        fields = ('id','name', 'alias')
