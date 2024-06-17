from django.db import models

class  Teacher(models.Model)
first_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length = 20)
   age= models.PositiveSmallIntegerField()
   gender = models.CharField(max_length =  20)
   nationality= models.CharField
   teacher_id=models.PositiveSmallIntegerField()
   email=models.EmailField
   year_of_birth=models.PositiveSmallIntegerField
   specilization=models.CharField()
   date_of_birth=models.DateField()


   def __str__(self):
    return f"{self.first_name} {self.last_name}"
    