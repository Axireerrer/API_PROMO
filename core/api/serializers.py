from rest_framework import serializers

from api.models import Advert


# Сериализатор для API
class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ['advert_id', 'title', 'author', 'views_count', 'position']



