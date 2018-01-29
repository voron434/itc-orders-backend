from rest_framework import serializers

from . import models


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = [
            'title',
            'description',
            'status',
        ]


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = '__all__'


class ProjectUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = [
            'title',
            'id',
        ]
