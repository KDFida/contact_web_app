# Import Django's forms module which provides tools for creating form classes.
from django import forms

# Import the Contact model from the current app's models file.
from .models import Contact

# Define a form class named ContactForm that inherits from Django's ModelForm.
# A ModelForm automatically generates form fields based on the fields of a specified model.
class ContactForm(forms.ModelForm):
    
    # The Meta class is used to specify metadata options for the form.
    class Meta:
        # Specify that this form is associated with the Contact model.
        model = Contact
        
        # Define the list of model fields to include in the form.
        # Only 'full_name', 'address', and 'phone_number' will be rendered as form inputs.
        fields = ['full_name', 'address', 'phone_number']
