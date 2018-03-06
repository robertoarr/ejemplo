from rest_framework import serializers
from mobile_api.player_dao import PlayerDao


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ""
        fields = "__all__"


class UserGetSerializer(serializers.Serializer):

    def list(self):
        result = PlayerDao.list(self.data)
        return result

    def retrieve(self):
        pass

    def delete(self):
        pass
