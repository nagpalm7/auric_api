from .models import *
from rest_framework import serializers
from django.contrib import auth
from django.utils import timezone
import datetime
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError


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

        username = validated_data.get('username')
        password = validated_data.get('password')
        validated_data.pop('username')
        validated_data.pop('password')
        try:
            django_user_obj = DjangoUser.objects.create(username=username)
        except IntegrityError as e:
            raise ValidationError(str(e))
        django_user_obj.set_password(password)
        django_user_obj.save()
        validated_data['auth_user'] = django_user_obj

        return User.objects.create(**validated_data)

    def to_internal_value(self, data):
        """
        do nothing in to_internal_value, i.e. do not trim off the invalid fields
        """
        return data

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
        read_only_fields = ('created_on',)


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print(validated_data)
        return FormSubmission.objects.create(**validated_data)

    def to_internal_value(self, data):
        """
        do nothing in to_internal_value, i.e. do not trim off the invalid fields
        """
        return data