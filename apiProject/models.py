from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=6,)
    dob = models.CharField(max_length=10, null=True, blank=True, verbose_name='Date of Birth')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}'s Profile"