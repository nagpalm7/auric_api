from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .permissions import *

##########################
# User Views
##########################

class UserList(APIView):
    permission_classes = [IsAdminOrReadOnly,]

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
    permission_classes = [IsAdminOrReadOnly,]

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
        current_user = User.objects.get(auth_user = request.user)
        if request.GET.get('onlyMy'):
            forms = FormSubmission.objects.filter(user = current_user)
        else:
            forms = FormSubmission.objects.all()
        serializer = FormSubmissionSerializer(forms, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format = None):
        # check if form is already submitted today from same location and city
        current_user = User.objects.get(auth_user = request.user)
        existing_submission = FormSubmission.objects.filter(user = current_user, city= request.data.get('city'), location= request.data.get('location') , created_on=timezone.now().today())
        if existing_submission.count() > 0:
            raise ValidationError('Not allowed')

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