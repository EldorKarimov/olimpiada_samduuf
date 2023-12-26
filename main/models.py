from django.db import models

class ContactUs(models.Model):
    full_name = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 15)
    subject = models.CharField(max_length = 150)
    message = models.TextField()

    def __str__(self):
        return self.full_name
    