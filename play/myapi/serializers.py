from rest_framework import serializers

from play.myapi.models import Hero


class HeroSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Hero
        fields = ('id','name', 'alias')

    def name_validate(self, name):

        if name is None:
            raise _("name can not blanl")

        return name    