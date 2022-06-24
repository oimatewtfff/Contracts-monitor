from rest_framework import viewsets

from .models import Contracts
from .serializers import ContractSerializer


class ContractsViewset(viewsets.ModelViewSet):
    serializer_class = ContractSerializer
    queryset = Contracts.objects.all()
