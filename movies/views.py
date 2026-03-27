from rest_framework import generics
from movies.models import Movies
from movies.serializers import MovieModelSerializer


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieModelSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieModelSerializer
