from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13) # +447000000000 - 13 digits with international code
    
    def __str__(self):
        return self.full_name
