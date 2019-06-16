from .models import *
from rest_framework import serializers
from django.contrib import auth
from django.utils import timezone
import datetime

class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.SerializerMethodField()
    class Meta:
    	model = User
    	fields = ('pk', 'name', 'typeOfUser', 'username')

    def get_username(self, obj):
        return obj.auth_user.username

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.userType = validated_data.get('userType', instance.userType)
        instance.save()
        return instance

class FormSubmissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = FormSubmission
    	fields = '__all__'