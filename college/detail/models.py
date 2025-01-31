from django.db import models

class CollegeModel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    established_year = models.IntegerField()
    
    class Meta:
        db_table="detail"


# Create your models here.
