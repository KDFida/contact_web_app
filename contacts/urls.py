# Import the 'path' function to define URL patterns.
from django.urls import path

# Import the views module from the current package. This allows us to reference the view functions.
from . import views

# Define the application namespace. This is useful when referring to URLs from templates or other URL configurations.
# The namespace helps distinguish these URLs from others when multiple apps are used.
app_name = 'contacts'

# Define the URL patterns for the contacts app.
urlpatterns = [
    # URL pattern for the contact list view:
    # When the URL is the root of this app (e.g., '/contacts/'), call the 'contact_list' view.
    # The name 'contact_list' can be used for URL reversing in templates.
    path('', views.contact_list, name='contact_list'),

    # URL pattern for adding a contact:
    # When the URL is '/add/' (e.g., '/contacts/add/'), call the 'add_contact' view.
    # This URL is named 'add_contact' for use in URL reversing.
    path('add/', views.add_contact, name='add_contact'),

    # URL pattern for the API endpoint:
    # When the URL is '/api/' (e.g., '/contacts/api/'), call the 'api_contacts' view.
    # This provides a JSON API for retrieving contacts and is named 'api_contacts'.
    path('api/', views.api_contacts, name='api_contacts'),
]
