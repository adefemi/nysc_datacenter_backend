from rest_framework import viewsets, permissions
from .serializers import section_model, sectionSerializer

class sectionViewSet(viewsets.ModelViewSet):
    queryset = section_model.objects.all()
    serializer_class = sectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)