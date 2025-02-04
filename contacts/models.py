# Import the models module from Django, which provides the base classes for defining models.
from django.db import models

# Define the Contact model, which represents a contact entry in the database.
class Contact(models.Model):
    # 'full_name' is a character field with a maximum length of 100 characters.
    full_name = models.CharField(max_length=100)
    
    # 'address' is a text field that can store longer text.
    # 'blank=True' means this field is optional (i.e., it can be left empty).
    address = models.TextField(blank=True)
    
    # 'phone_number' is a character field with a maximum length of 13 characters.
    # This is designed to hold phone numbers formatted like "+447000000000" (13 digits including the international code).
    phone_number = models.CharField(max_length=13)
    
    # The __str__ method defines the string representation of the Contact object.
    # When you print a Contact instance, it will return the full_name.
    def __str__(self):
        return self.full_name
