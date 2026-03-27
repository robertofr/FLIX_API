from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movies

class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movies
        fields = '__all__'

    def get_rate(self, obj):
       rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
       
       if rate: 
           return round(rate, 1)

       return None    

    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1950.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 255:
            raise serializers.ValidationError('O resumo não deve ser maior que 255 caracteres.')
        return value
    
    