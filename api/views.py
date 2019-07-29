from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .permissions import *
from datetime import date

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

class GetUser(APIView):
    def get(self, request, format = None):
        user = User.objects.get(auth_user = request.user)
        serializer = UserSerializer(user)
        return Response(serializer.data)

##########################
# Form Views
##########################

class FormSubmissionList(APIView):

    def get(self, request, format = None):
        current_user = User.objects.get(auth_user = request.user)
        if request.GET.get('onlyMy'):
            forms = FormSubmission.objects.filter(user = current_user, created_on=date.today())
        else:
            forms = FormSubmission.objects.filter(created_on=date.today() )
        serializer = FormSubmissionSerializer(forms, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format = None):
        required_fields = [
            'group', 
            'location', 
            'mind_o', 
            'skin_o', 
            'body_o',
            'multipack_o',
            'mind_c', 
            'skin_c', 
            'body_c',
            'multipack_c',
            'jumbo_combos']

        for field in required_fields:
            if field not in request.data:
                raise ValidationError('Not allowed, field missing')

        # check if form is already submitted today from same location
        current_user = User.objects.get(auth_user = request.user)
        existing_submission = FormSubmission.objects.filter(
            user=current_user,
            location=request.data.get('location'),
            created_on=date.today(),
        )
        if existing_submission.count() > 0:
            raise ValidationError('Not allowed')

        request.data['group'] = Group.objects.get(pk = request.data.get('group'))
        request.data['location'] = Location.objects.get(pk = request.data.get('location'))
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
        request.data['group'] = Group.objects.get(pk = request.data.get('group'))
        request.data['location'] = Location.objects.get(pk = request.data.get('location'))
        serializer = FormSubmissionSerializer(form, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        form = self.get_object(pk)
        form.delete()
        return Response(status=HTTP_204_NO_CONTENT)

##########################
# City Views
##########################

class CityList(APIView):
    def get(self, request, format = None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CityDetail(APIView):
    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        city = self.get_object(pk)
        serializer = CitySerializer(city,  context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        city = self.get_object(pk)
        serializer = CitySerializer(city, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        city = self.get_object(pk)
        city.delete()
        return Response(status=HTTP_204_NO_CONTENT)

##########################
# Trade Views
##########################

class TradeList(APIView):
    def get(self, request, format = None):
        trades = Trade.objects.all()
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = TradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TradeDetail(APIView):
    def get_object(self, pk):
        try:
            return Trade.objects.get(pk=pk)
        except Trade.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        trade = self.get_object(pk)
        serializer = TradeSerializer(trade,  context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        trade = self.get_object(pk)
        serializer = TradeSerializer(trade, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        trade = self.get_object(pk)
        trade.delete()
        return Response(status=HTTP_204_NO_CONTENT)

##########################
# Location Views
##########################

class LocationList(APIView):
    def get(self, request, format = None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True,  context={'request': request})
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = LocationSerializer(data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location,  context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data,  context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        location = self.get_object(pk)
        location.delete()
        return Response(status=HTTP_204_NO_CONTENT)

##########################
# Group Views
##########################

class GroupList(APIView):
    def get(self, request, format = None):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True,  context={'request': request})
        return Response(serializer.data)

    def post(self, request, format = None):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupDetail(APIView):
    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        group = self.get_object(pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        group = self.get_object(pk)
        group.delete()
        return Response(status=HTTP_204_NO_CONTENT)

##########################
# Daily Report Views
##########################

class Reports(APIView):
    def get(self, request, format = None):
        reports = []
        if request.GET.get('filter') == 'location':
            forms = FormSubmission.objects.filter(created_on = date.today())
            locations = Location.objects.all()
            for location in locations:
                sales = 0
                for form in forms:
                    if location == form.location:
                        sales = sales + int(form.sales)
                report = {
                    "location" : location.location,
                    "sales": sales
                }
                reports.append(report)      
        elif request.GET.get('filter') == 'group':
            forms = FormSubmission.objects.filter(
                group = request.GET.get('group'),
                created_on = date.today())
            users = User.objects.all()
            for user in users:
                sales = 0
                count = 0
                for form in forms:
                    if user == form.user:
                        sales = sales + int(form.sales)
                        count = count + 1
                try:
                    productivity = float(sales/count)
                except ZeroDivisionError:
                    productivity = 0
                report = {
                    "user" : user.name,
                    "sales": sales,
                    "productivity": productivity,
                }
                reports.append(report) 
        return Response(reports)