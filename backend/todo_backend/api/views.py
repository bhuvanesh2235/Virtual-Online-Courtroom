from rest_framework import generics
from .models import Case
from .serializers import CaseSerializer

class CaseListCreate(generics.ListCreateAPIView):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
