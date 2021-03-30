from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from play.myapi.serializers import HeroSerializer
from play.myapi.models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [IsAuthenticated]
    


