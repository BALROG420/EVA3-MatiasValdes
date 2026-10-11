from rest_framework import serializers
from posts.models import Banda


class BandaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banda
        fields = '__all__'