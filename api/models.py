from django.db import models
from django.contrib.auth.models import User as DjangoUser
userTypes = ( ('intern','intern'),('admin','admin') )
locations = ( ('Delhi','Delhi'),('Tricity','Tricity') )
cities = ( ('Delhi','Delhi'),('Tricity','Tricity') )

class User(models.Model):
	name = models.CharField(max_length = 100, blank = False, null = False, unique = False)
	typeOfUser = models.CharField(max_length=10,choices=userTypes,default='intern')
	auth_user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
	
	def __str__(self):
		if self.name:
			return str(self.name)
		else:
			return self.AuthUser.username
	class Meta:
		ordering = ["name"]

class FormSubmission(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=100,choices=locations)
	city = models.CharField(max_length=100, choices=cities)
	mind_o = models.IntegerField()
	body_o = models.IntegerField()
	skin_o = models.IntegerField()
	multipack_o = models.IntegerField()
	mind_c = models.IntegerField()
	body_c = models.IntegerField()
	skin_c = models.IntegerField()
	multipack_c = models.IntegerField()
	jumbo_combos = models.IntegerField()
	images = models.ImageField(blank=True,null=True)
