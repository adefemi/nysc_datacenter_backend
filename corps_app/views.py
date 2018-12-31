from rest_framework import viewsets, permissions
from .serializers import Members_app, corpsSerializer

class corpsViewSet(viewsets.ModelViewSet):
    queryset = Members_app.objects.all()
    serializer_class = corpsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)