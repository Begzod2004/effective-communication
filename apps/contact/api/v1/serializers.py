from rest_framework import serializers
from apps.contact.models import Communication, CategoryProblem


class CommunicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Communication
        fields = '__all__'


class CategoryProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryProblem
        fields = '__all__'

