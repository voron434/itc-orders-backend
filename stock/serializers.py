from rest_framework import serializers

from . import models


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = [
            'id',
            'title',
            'description',
            'status',
        ]


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = [
            'id',
            'title',
            'description',
            'status',
        ]


class ProjectUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = [
            'title',
            'id',
        ]
