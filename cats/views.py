from rest_framework.generics import ListCreateAPIView
from .serializers import CatsSerializer
from .models import Cat


class CatView(ListCreateAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatsSerializer
