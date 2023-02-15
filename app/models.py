from django.db import models

# class StudentImage(models.Model):
#     std_id=models.CharField(max_length=5,blank=False)
#     image=models.ImageField(upload_to='image',blank=False)
#
#     def __str__(self):
#         return f"{self.id}"


class Attendence(models.Model):
    std_id=models.CharField(max_length=5,blank=False)
    time=models.CharField(max_length=30,blank=False)
    date=models.CharField(max_length=30,blank=False)

    def __str__(self):
        return f"{self.std_id}"
