from rest_framework import viewsets
from rest_framework import permissions
<<<<<<< HEAD
from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_framework.response import Response

from players.models import Player
from players.serializers import PlayerSerializer
# Test test
# Another test
# fix
=======
from rest_framework.response import Response
from players.models import Player
from django.contrib.auth.models import User
from players.serializers import RegisterSerializer, UpdateUserSerializer
from django.http import Http404

>>>>>>> develop


class PlayerViewSet(viewsets.GenericViewSet):
<<<<<<< HEAD
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = []
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filter_fields = ("")

    def list(self, request):
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
=======
    queryset = Player.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny, )

    def create(self, request, *args, **kwargs):
        """Creates an user from the Django model"""
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"Message": "Usuario creado"})

    def partial_update(self, request, pk):
        """Handles updating part of an object"""
        try:
            print("Este es es el pk \"{}\"".format(pk))
            user = Player.objects.get(pk=pk)
            serializer = UpdateUserSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Player.DoesNotExist:
            raise Http404("Not found")


    def list(self, request):
        pass
>>>>>>> develop

    def retrieve(self, request, pk):
        pass

    def delete(self, request, pk):
        pass


# class PlayerViewSet(viewsets.GenericViewSet):
#     permission_classes = []
#     authentication_classes = []
#
#     def list(self, request):
#
#         pass
#
#     def retrieve(self, request, pk):
#         pass
#
#     def create(self, request):
#         pass
#
#     def partial_update(self, request, pk):
#         pass
#
#     def delete(self, request, pk):
#         pass
