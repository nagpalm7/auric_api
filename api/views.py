from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

##########################
# User Views
##########################

class UserList(APIView):
    def get(self, request, format = None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):

	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

	def get(self, request, pk, format = None):
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format = None):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format = None):
		user = self.get_object(pk)
		user.delete()
		return Response(status=HTTP_204_NO_CONTENT)

##########################
# Form Views
##########################

class FormSubmissionList(APIView):
    def get(self, request, format = None):
        forms = FormSubmission.objects.all()
        serializer = FormSubmissionSerializer(forms, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = FormSubmissionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormSubmissionDetail(APIView):

	def get_object(self, pk):
		try:
			return FormSubmission.objects.get(pk=pk)
		except FormSubmission.DoesNotExist:
			raise Http404

	def get(self, request, pk, format = None):
		form = self.get_object(pk)
		serializer = FormSubmissionSerializer(form, context={'request': request})
		return Response(serializer.data)

	def put(self, request, pk, format = None):
		form = self.get_object(pk)
		serializer = FormSubmissionSerializer(form, data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format = None):
		form = self.get_object(pk)
		form.delete()
		return Response(status=HTTP_204_NO_CONTENT)