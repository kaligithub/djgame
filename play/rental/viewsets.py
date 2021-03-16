from rest_framework import viewsets
from play.rental.models import Friend, Belonging, Borrowed
from play.rental.serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer



class FriendViewSet(viewsets.ModelViewSet):
    
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer

class BelongingViewSet(viewsets.ModelViewSet):

    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer

class BorrowedViewSet(viewsets.ModelViewSet):

    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer


