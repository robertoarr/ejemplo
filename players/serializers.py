from rest_framework import serializers
from players.models import Player



class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ""
        fields = "__all__"


class UserGetSerializer(serializers.Serializer):

    def list(self):
        pass

    def retrieve(self):
        pass

    def delete(self):
        pass


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

    # def validate_player_id(self, value):
    #     try:
    #         Player.objects.request(pk=value)
    #         return value
    #     except:
    #         serializer.ValidationError("El jugador no existe")

    # def get_serializer_class(self):
    #     if self.request.user.is_staff:
    #         return FullAccountSerializer
    #     return BasicAccountSerializer
