from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.db.models import Sum

class CLubAPIVIEW(APIView):
    def get(self,request,pk):
        club = Club.objects.get(id=pk)
        serializer = ClubSerializers(club)
        return Response(serializer.data)
class ClublarAPIVIEW(APIView):

    def get(self,request):
        clubs = Club.objects.annotate(umum_summa=Sum('futbolchilari__tr_narxi')).order_by('-umum_summa')
        serializer = ClubSerializers(clubs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlayersAPIVIEW(APIView):
    def get(self,request):
        player = Player.objects.all().order_by("-tr_narxi")
        serializer = PlayerSerializers(player, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TransferAPIVIEW(APIView):
    def get(self,request):
        transfer = Transfer.objects.all().order_by('narxi','tax_narxi')
        serializer = TransferSerializers(transfer, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class Hozirgi_mavsumsAPIVIEW(APIView):
    def get(self,request):
        mavsumlar = Hozirgi_mavsum.objects.all().order_by("hozirgi_mavsum")
        serializer = Hozirgi_mavsumSerializer(mavsumlar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class Mavsumga_oidAPIVIEW(APIView):
    def get(self,request,soz):
        transfer = Transfer.objects.filter(mavsum=soz)
        serializer = TransferSerializers(transfer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class u20ageAPIVIEW(APIView):
    def get(self,request):
        from datetime import date, timedelta
        bugun = date.today()
        boshi = bugun - timedelta(days=20 * 365)
        player = Player.objects.filter(t_yil__range=[boshi, bugun])
        serializer = PlayerSerializers(player, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class statsAPIVIEW(APIView):
    def get(self,request):
        transfer = Transfer.objects.all().order_by('narxi','tax_narxi')[0:100]
        serializer = TransferSerializers(transfer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





# Create your views here.
