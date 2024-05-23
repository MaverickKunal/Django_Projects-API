from rest_framework import serializers
#from rest_framework import Contact
from home.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Contact
        #fields = ('name','email')
        fields = '__all__'