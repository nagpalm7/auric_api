from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(FormSubmission)
admin.site.register(ImageSubmisson)
admin.site.register(City)
admin.site.register(Location)
admin.site.register(Group)
admin.site.register(Trade)
admin.site.register(CustomerInformation)