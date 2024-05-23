from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

from rest_framework import generics
from home.serializers import ContactSerializer

from rest_framework.views import APIView      # Related logic is commented
from rest_framework.response import Response    # Related logic is commented
from rest_framework import status              # Related logic is commented


#username-kunalverma; pass-123
# Create your views here.
def index(request):
    #return HttpResponse("Welcome to my Web")
    #return render(request, 'index.html') 
    context = {
        "variable" : "this is first variable",
        "variable1" : "this is second variable"
    }
    return render(request, 'index.html',context) 

def about(request):
    #return HttpResponse("This is my about page")
    return render(request, 'about.html') 

def services(request):
    #return HttpResponse("This is my service page")
    return render(request, 'services.html') 

def contact(request):
    #return HttpResponse("This is my contact page")
    #return render(request, 'contact.html') 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone number')
        query = request.POST.get('query')
        #date = request.POST.get('datetime')
        contact = Contact(name=name, email=email, phone=phone, query=query, date=datetime.today())
        contact.save()
        messages.success(request, "Your data is submitted")
    return render(request, 'contact.html') 


# class contactlist(APIView):

#     def get(self, request):  #helps fetch all data  (reading data)
#         contacts = Contact.objects.all()
#         serializer = ContactSerializer(contacts, many = True)
#         return HttpResponse(serializer.data)

#     def post(self):     #helps create a new data   (submitting data)
#         pass

class contactlist(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer