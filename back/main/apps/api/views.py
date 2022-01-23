from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import action, permission_classes
from rest_framework.response import Response

# JWT
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
from rest_framework import viewsets
from main.apps.booking.models import LoadingPort, DischargePort, Booking, Vehicle

from .serializer import LoadingPortSerializer, DischargePortSerializer, \
    VehicleSerializer, BookingSerializer

'''
# set a lifetime for token, custom token
from rest_framework_simplejwt.views import TokenViewBase
from .serializer import TokenObtainLifetimeSerializer, TokenRefreshLifetimeSerializer


class TokenObtainPairView(TokenViewBase):
    serializer_class = TokenObtainLifetimeSerializer


class TokenRefreshView(TokenViewBase):
    serializer_class = TokenRefreshLifetimeSerializer
'''

# ModelviewSet me permite put, get patch, put


class LoadingPortViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = LoadingPort.objects.all().order_by('id')
    serializer_class = LoadingPortSerializer


class DischargePortViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = DischargePort.objects.all().order_by('id')
    serializer_class = DischargePortSerializer


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Booking.objects.all().order_by('booking_number')
    serializer_class = BookingSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Vehicle.objects.all().order_by('pk_booking')
    serializer_class = VehicleSerializer
