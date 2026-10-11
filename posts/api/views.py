from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from posts.models import Banda
from .serializers import BandaSerializer


class BandaViewSet(viewsets.ModelViewSet):
    queryset = Banda.objects.all()
    serializer_class = BandaSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [IsAuthenticated()]
        return [IsAdminUser()]