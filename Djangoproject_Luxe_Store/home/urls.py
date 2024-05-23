from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "Kunal Store Admin"
admin.site.site_title = "Kunal Store Admin Portal"
admin.site.index_title = "Welcome to Kunal Store"

#method to be used in connecting view to url
urlpatterns = [
    path("", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("services", views.services, name = 'services'),
    path("contact", views.contact, name = 'contact')
]