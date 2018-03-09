from rest_framework import serializers
# from mobile_api.player_dao import PlayerDao
from players.models import Player
from django.contrib.auth.models import User


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


class UpdateUserSerializer(serializers.ModelSerializer):
    """Edits or completes the inf. of the player registered"""

    phone_number = serializers.CharField(max_length=10, required=True)
    nickname = serializers.CharField(max_length=20)
    gender = serializers.ChoiceField(choices=Player.GENDER_CHOICES)
    dob = serializers.DateField(default=None)
    web_site = serializers.CharField(max_length=400)

    class Meta:
        model = User
        fields = ('email', 'username', 'phone_number', 'nickname', 'gender', 'dob', 'web_site')
        extra_kwargs = {
            'username': {
                'required': False
            },
        }

    def update(self, instance, validated_data):
        instance.user.username = validated_data.get('username', instance.user.username)
        instance.user.email = validated_data.get('email', instance.user.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.nickname = validated_data.get('nickname', instance.nickname)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.web_site = validated_data.get('web_site', instance.web_site)
        instance.save()

        return instance

class UserGetSerializer(serializers.Serializer):

    def list(self):
        result = PlayerDao.list(self.data)
        return result

    def retrieve(self):
        pass

    def delete(self):
        pass
