from django.db import models


# Create your models here.

class Departments(models.Model):
    department_name=models.CharField(max_length=100)
    department_info=models.TextField()

    def __str__(self):
        return self.department_name
    
class Doctors(models.Model):
    doc_name=models.CharField(max_length=250)
    specialization=models.CharField(max_length=250)
    department_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    
class UserBooking(models.Model):
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    email=models.EmailField()
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now_add=True)


    


