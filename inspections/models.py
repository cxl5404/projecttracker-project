from django.db import models

# Project Class
class Inspection(models.Model):
  
     address = models.CharField(max_length=255)
     city = models.CharField(max_length=255)
     state = models.CharField(max_length=255)
     zip_Code = models.CharField(max_length=255)
     pub_date = models.DateTimeField()

     Permit_Num = models.IntegerField(default=0)
     Type_of_Inspection = models.CharField(max_length=255)
     Step = models.CharField(max_length=255)
     Inspection_Time = models.CharField(max_length=255, default="00/00/0000")
     Inspector_Name = models.CharField(max_length=255)
     District = models.CharField(max_length=255, default="Central District")
     phone_Number = models.CharField(max_length=255)
     Result = models.CharField(max_length=255, default="In Progress")


     def __str__(self):
         return self.address + " " + self.state
