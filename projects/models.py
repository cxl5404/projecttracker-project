from django.db import models
from django.contrib.auth.models import User

# Project Class
class Project(models.Model):
     customer_Name = models.CharField(max_length=255)
     phone_Number = models.CharField(max_length=255)
     address = models.CharField(max_length=255)
     city = models.CharField(max_length=255)
     state = models.CharField(max_length=255)
     zip_Code = models.CharField(max_length=255)
     pub_date = models.DateTimeField()
     building_Permit_Num = models.IntegerField(default=0)
     BP_Status = models.IntegerField(default=0)
     plumbing_Permit_Num = models.IntegerField(default=0)
     PP_Status = models.IntegerField(default=0)
     electric_Permit_Num = models.IntegerField(default=0)
     EP_Status = models.IntegerField(default=0)
     zoning_Permit_Num = models.IntegerField(default=0)
     ZP_Status = models.IntegerField(default=0)
     mechanical_Permit_Num = models.IntegerField(default=0)
     MP_Status = models.IntegerField(default=0)
     sign_Permit_Num = models.IntegerField(default=0)
     SP_Status = models.IntegerField(default=0)

     def __str__(self):
         return self.address + " " + self.state


     def pub_date_pretty(self):
         return self.pub_date.strftime('%m-%e-%Y')
