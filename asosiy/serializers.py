from rest_framework import serializers
from .models import *


class PlayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"




class ClubSerializers(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"

    def to_representation(self, instance):
        club = super().to_representation(instance)
        club['player'] = PlayerSerializers(Player.objects.filter(club=instance), many=True).data
        return club





class TransferSerializers(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = "__all__"


class Hozirgi_mavsumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hozirgi_mavsum
        fields = "__all__"


