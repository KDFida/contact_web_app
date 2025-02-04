# Import Django shortcut functions for rendering templates and redirecting users.
from django.shortcuts import render, redirect

# Import JsonResponse for sending JSON data in responses (useful for AJAX or API endpoints).
from django.http import JsonResponse

# Import the Contact model to interact with the contacts table in the database.
from .models import Contact

# Import the ContactForm form class to handle user input for creating new contacts.
from .forms import ContactForm

# -----------------------------------------------------------------------------
# View function to display a list of contacts.
# -----------------------------------------------------------------------------
def contact_list(request):
    # Retrieve all Contact objects from the database.
    contacts = Contact.objects.all()
    
    # Render the 'contact_list.html' template located in the 'contacts' templates directory,
    # passing the retrieved contacts in a context dictionary.
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

# -----------------------------------------------------------------------------
# View function to add a new contact.
# -----------------------------------------------------------------------------
def add_contact(request):
    # Check if the form is submitted via POST request.
    if request.method == "POST":
        # Instantiate the ContactForm with data from the POST request.
        form = ContactForm(request.POST)
        
        # Validate the form data.
        if form.is_valid():
            # Save the valid form data to create a new Contact object in the database.
            contact = form.save()
            
            # Check if the request is an AJAX request by inspecting the 'x-requested-with' header.
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Prepare a dictionary with contact details to send back as a JSON response.
                data = {
                    'contact_id': contact.id,
                    'full_name': contact.full_name,
                    'address': contact.address,
                    'phone_number': contact.phone_number,
                }
                # Return a JsonResponse containing the contact data.
                return JsonResponse(data)
            else:
                # If not an AJAX request, redirect the user to the contact list view.
                return redirect('contacts:contact_list')
    else:
        # For GET requests, instantiate an empty ContactForm.
        form = ContactForm()
    
    # Render the 'add_contact.html' template and pass the form instance to it.
    return render(request, 'contacts/add_contact.html', {'form': form})

# -----------------------------------------------------------------------------
# View function that serves as a simple API endpoint for retrieving contacts.
# -----------------------------------------------------------------------------
def api_contacts(request):
    # Retrieve all Contact objects from the database.
    contacts = Contact.objects.all()
    
    # Build a list of dictionaries, each containing selected details of a contact.
    data = [
        {
            'contact_id': contact.id,
            'full_name': contact.full_name,
            'address': contact.address,
            'phone_number': contact.phone_number,
        }
        for contact in contacts
    ]
    
    # Return the data as a JSON response. The 'safe=False' parameter allows lists to be returned.
    return JsonResponse(data, safe=False)
