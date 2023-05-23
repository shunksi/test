from rest_framework import viewsets, mixins
from partner.models import Partner
from partner.serializer import PartnerSerializer
from django.views.generic import ListView, DetailView

class PartnerView(ListView):
    model = Partner
    queryset = Partner.objects.all()
    context_object_name = 'partner'


class AllPartnerView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerDetailsView(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
