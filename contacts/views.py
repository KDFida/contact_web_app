from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                data = {
                    'contact_id': contact.id,
                    'full_name': contact.full_name,
                    'address': contact.address,
                    'phone_number': contact.phone_number,
                }
                return JsonResponse(data)
            else:
                return redirect('contacts:contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def api_contacts(request):
    contacts = Contact.objects.all()
    data = [
        {
            'contact_id': contact.id,
            'full_name': contact.full_name,
            'address': contact.address,
            'phone_number': contact.phone_number,
        }
        for contact in contacts
    ]
    return JsonResponse(data, safe=False)