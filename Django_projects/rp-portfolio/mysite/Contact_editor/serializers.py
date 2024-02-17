from rest_framework import serializers

from .models import ContactText

class ContactTextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactText
        fields = ('id', 'first_name', 'last_name', 'company_name', 
                  'academic_title',  'position', 'street', 'house_number', 'adress_detail', 'zip', 'city', 'region', 'country', 'email','phone_number', 'mobile_phone_number', 'fax_number', 'web_site', 'facebook', 'linkedin')
        
# class AccountSerializer(serializers.ModelSerializer):
#     url = serializers.CharField(source='get_absolute_url', read_only=True)

#     class Meta:
#         model = Account