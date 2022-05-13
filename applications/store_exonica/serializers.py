from rest_framework import serializers


class CountCarSerializar(serializers.Serializer):

    total = serializers.IntegerField()

