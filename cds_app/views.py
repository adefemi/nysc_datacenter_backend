from rest_framework import viewsets, permissions
from .serializers import cds_model, cdsSerializer

class cdsViewSet(viewsets.ModelViewSet):
    queryset = cds_model.objects.all()
    serializer_class = cdsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)