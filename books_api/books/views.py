from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters
from .filters import BookFilter
from .models import Book
from .pagination import CustomPagination
from .serializers import BookSerializer


class ListCreateBookAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    # pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter


class RetrieveUpdateDestroyBookAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
