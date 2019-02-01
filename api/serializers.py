from rest_framework import serializers
from api.models import MovementHistory
from api.models import Names

# class NamesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Names
#         fields = '__all__'
#
# class StringListField(serializers.ListField):
#     child = serializers.CharField()

class MovementHistorySerializer(serializers.ModelSerializer):
    # personNames = serializers.PrimaryKeyRelatedField(many=True, queryset=Names.objects.all())
    class Meta:
        model = MovementHistory
        fields = '__all__'