from django.db import models

class Course(models.Model):

Course_name = models.CharField()
Course_description=models.CharField()
Course_level = models.CharField()
Course_duration=models.PositiveSmallIntegerField()
Course_objective=models.CharField()
Course_module=models.CharField()
Course_prior_skills=models.CharField()
Course_learning_materials = models.CharField()
Course_trainer = models.CharField()
course_attentance_per_week=models.PositiveSmallIntegerField()

def__str__(self):
    return f"{self.Course_name}  {self.Course_description}"

