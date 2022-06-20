from rest_framework import serializers

from petclub.models import Pet

#Serializar es estandarizar, dejarlo en JSON
#Deserializar pasarlo nuevamente a python
class CustomPetSerializer(serializers.Serializers):
    name = serializers.CharField()
    specie = serializers.CharField()

    class Meta:
        model = Pet
