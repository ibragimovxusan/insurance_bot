from datetime import timedelta, datetime

from django.shortcuts import get_object_or_404
from rest_framework import status, mixins, viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta

from ..models import InsurancePeriod, CarDriver, Account
from .serializers import InsurancePeriodSerializer, AccountSerializer, CarDriverSerializer


class InsurancePeriodListView(generics.ListAPIView):
    queryset = InsurancePeriod.objects.all()
    serializer_class = InsurancePeriodSerializer


class CarDriverListView(generics.ListAPIView):
    queryset = CarDriver.objects.all()
    serializer_class = CarDriverSerializer


class AccountCreateAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
