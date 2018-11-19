from django.db import models

# Create your models here.
class Division(models.Model):
    div_name = models.CharField(max_length=50)
    div_population = models.IntegerField()
    div_area = models.IntegerField()

    def __str__(self):
        return self.div_name
class District(models.Model):
    dis_name = models.CharField(max_length=50)
    dis_population = models.IntegerField()
    dis_area = models.IntegerField()
    div = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return self.dis_name
