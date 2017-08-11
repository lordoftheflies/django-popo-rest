from rest_framework import serializers


class PopoFooSerializer(serializers.Serializer):
    first = serializers.CharField(required=False, allow_blank=True, max_length=100)
    last = serializers.CharField(required=False, allow_blank=True, max_length=100)