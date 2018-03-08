from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from players.models import Player
from players.serializers import RegisterSerializer


class PlayerViewSet(viewsets.GenericViewSet):
    queryset = Player.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):
        """Creates an user from the Django model"""
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"Message": "Usuario creado"})

    def list(self, request):
        pass

    def partial_update(self, request, pk):
        pass

    def retrieve(self, request, pk):
        pass

    def delete(self, request, pk):
        pass
