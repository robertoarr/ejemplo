from rest_framework import serializers
<<<<<<< HEAD
from players.models import Player

=======
# from mobile_api.player_dao import PlayerDao
from players.models import Player
from django.contrib.auth.models import User
>>>>>>> develop


class RegisterSerializer(serializers.ModelSerializer):
    """Creates an user from the Django model"""

    phone_number = serializers.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'phone_number')
        extra_kwargs = {
            'email': {
                'required': True,
                'allow_blank': False
            },
        }

    def create(self, validated_data):
        userauth = User.objects.create_user(username=validated_data.get('username'),
                                            password=validated_data.get('password'),
                                            email=validated_data.get('email'),
                                            is_active=1, is_superuser=0)
        player = Player(user=userauth, phone_number=self.data.get("phone_number"))
        player.save()

        return player


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
