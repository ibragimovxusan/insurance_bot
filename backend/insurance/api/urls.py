from django.urls import path
from .views import InsurancePeriodListView, CarDriverListView, AccountCreateAPIView


urlpatterns = [
    path('insurances', InsuranceListView.as_view(), name='insurances'),
    path('user/', AccountCreateAPIView.as_view(), name='create_user')
]