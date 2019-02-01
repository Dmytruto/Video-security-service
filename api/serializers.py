from rest_framework import serializers
from api.models import MovementHistory
from api.models import Names

class NamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Names
        fields = '__all__'


class MovementHistorySerializer(serializers.ModelSerializer):
    authors = NamesSerializer(read_only=True, many=True)
    class Meta:
        model = MovementHistory
        fields = '__all__'