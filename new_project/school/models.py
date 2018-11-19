from django.db import models

# Create your models here.

class Gurdian(models.Model):
    gurdian_id = models.IntegerField(unique=True)
    gurdian_name = models.CharField(max_length=50)
    gender_choose = (('m','male'),('f','female'))
    gurdian_gender = models.CharField(max_length=50,choices = gender_choose)
    gurdian_age = models.IntegerField()
    gurdian_phone = models.IntegerField(unique=True)

    def __str__(self):
        return self.gurdian_name

class StudentClass(models.Model):
    name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name

class StudenInfo(models.Model):
    student_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    roll = models.IntegerField(unique=True)
    std_class = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    gender_choice = (('m', 'male'), ('f', 'female'))
    gender = models.CharField(max_length=50, choices=gender_choice)
    age = models.IntegerField()
    guard = models.OneToOneField(Gurdian, on_delete=models.SET_NULL, blank=True, null=True)

    class meta:
        unique_together=('std_class','roll')

    def __str__(self):
            return self.name
class StudentProfile(models.Model):
    s_photo = models.ImageField()
    s_address = models.CharField(max_length=50)
    s_phone = models.CharField(max_length=50)
    s_blood = models.CharField(max_length=50)
    std = models.OneToOneField(StudenInfo, on_delete=models.CASCADE)
    def __str__(self):
            return self.std.name


