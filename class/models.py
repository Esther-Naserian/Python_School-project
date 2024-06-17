from django.db import models

class Class(models.Model):
    class_name=models.CharField()
    class_color=models.CharField()
    class_building_materials=models.CharField()
    class_size =models.CharField()
    class_capacity=models.PositiveSmallIntegerField()
    class_lightning=models.CharField()
    class_temperature=models.CharField()
    class_odor=models.CharField()
    class_comfort=models.CharField()
    class_state=models.CharField()

    def __str__(self):
        return f"{self.class_name} {self.class_color}"

