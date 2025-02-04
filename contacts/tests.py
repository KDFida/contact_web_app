from django.test import TestCase
from .models import Contact
from django.urls import reverse

class ContactModelTest(TestCase):
    def setUp(self):
        # Create a sample Contact object
        self.contact = Contact.objects.create(
            full_name="John Doe",
            address="123 Main St",
            phone_number="+447000000000"
        )
    
    def test_contact_str(self):
        # Test that the __str__ method returns the full_name
        self.assertEqual(str(self.contact), "John Doe")

class ContactListViewTest(TestCase):
    def setUp(self):
        # Create a contact to display on the list view
        Contact.objects.create(
            full_name="Jane Doe",
            address="456 Side St",
            phone_number="+447123456789"
        )
    
    def test_contact_list_view_status_code(self):
        # Get the URL for the contact list using reverse URL resolution
        response = self.client.get(reverse('contacts:contact_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_contact_list_view_content(self):
        # Verify that the page contains the contact's full name
        response = self.client.get(reverse('contacts:contact_list'))
        self.assertContains(response, "Jane Doe")

