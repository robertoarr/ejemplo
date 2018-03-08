from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_framework.response import Response

from players.models import Player
from players.serializers import PlayerSerializer
# Test test
# Another test
# fix


class PlayerViewSet(viewsets.GenericViewSet):
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

    def partial_update(self, request, pk):
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
