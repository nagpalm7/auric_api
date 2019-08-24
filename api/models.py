from django.db import models
from django.contrib.auth.models import User as DjangoUser
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from datetime import date

userTypes = ( ('intern','intern'),('admin','admin') )

class User(models.Model):
    name = models.CharField(max_length = 100, blank = False, null = False, unique = False)
    typeOfUser = models.CharField(max_length=10,choices=userTypes,default='intern')
    auth_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    
    def __str__(self):
        if self.name:
            return str(self.name)
        else:
            return self.auth_user.username
    class Meta:
        ordering = ["name"]

class City(models.Model):
    city = models.CharField(max_length=100, blank = False, null = False)
    def __str__(self):
        return str(self.city)

class Trade(models.Model):
    trade = models.CharField(max_length=100, blank = False, null = False)
    def __str__(self):
        return str(self.trade)

class Group(models.Model):
    group = models.CharField(max_length=100, blank = False, null = False)
    
    def __str__(self):
        return str(self.group)

class Location(models.Model):
    city =  models.ForeignKey(City, on_delete = models.CASCADE)
    location = models.CharField(max_length=100, blank = False, null = False)
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    trade = models.ForeignKey(Trade, on_delete = models.CASCADE)
    def __str__(self):
        return str(self.location)

class FormSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    sales = models.CharField(max_length=100,default='0')
    mind_o = models.CharField(max_length=100, blank = False, null = False)
    body_o = models.CharField(max_length=100, blank = False, null = False)
    skin_o = models.CharField(max_length=100, blank = False, null = False)
    multipack_o = models.CharField(max_length=100, blank = False, null = False)
    mind_c = models.CharField(max_length=100, blank = False, null = False)
    body_c = models.CharField(max_length=100, blank = False, null = False)
    skin_c = models.CharField(max_length=100, blank = False, null = False)
    multipack_c = models.CharField(max_length=100, blank = False, null = False)
    num_samplings = models.CharField(max_length=100, blank = False, null = False)
    jumbo_combos = models.CharField(max_length=100, blank = False, null = False)
    comment = models.CharField(max_length=100, blank = True, null = True)
    created_on = models.DateField(default = date.today, editable=False)

    def save(self, *args, **kwargs):
        self.sales = (int(self.mind_o) - int(self.mind_c)) + (int(self.body_o) - int(self.body_c)) + (int(self.skin_o) - int(self.skin_c)) + ((int(self.multipack_o) - int(self.multipack_c)))*3
        super().save(*args, **kwargs)

class CustomerInformation(models.Model):
    form_submission = models.ForeignKey(FormSubmission, on_delete = models.CASCADE)
    name = models.CharField(max_length=100, blank = False, null = False)
    email = models.CharField(max_length=100, blank = False, null = False)
    address = models.CharField(max_length=100, blank = False, null = False)
    number = models.CharField(max_length=100, blank = False, null = False)
    mind = models.CharField(max_length=100, blank = False, null = False)
    body = models.CharField(max_length=100, blank = False, null = False)
    skin = models.CharField(max_length=100, blank = False, null = False)
    multipack = models.CharField(max_length=100, blank = False, null = False)

class ImageSubmisson(models.Model):
    form_submission = models.ForeignKey(FormSubmission, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='submission_images/')
