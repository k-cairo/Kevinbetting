from rest_framework import serializers
from Website.models import MatchsAVenir, Iframe, Data


class MatchsAVenirSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchsAVenir
        fields = '__all__'


class IframeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iframe
        fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
