from django.shortcuts import render
from django.contrib import messages
from Contact_editor.models import ContactText
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .serializers import ContactTextSerializer
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ContactText
import os
import openai
from dotenv import load_dotenv
import re
import json

# Create your views here.
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
def configure():
    load_dotenv(    )

def api_call(input, prompt=""):
    configure()
    api_key = os.getenv('api_key')
    openai.api_key = api_key
    # pwd = os.path.dirname(__file__)
    # contacts = open(pwd + '/contacts.txt')
    sentence1 = '''\nI want to extract my input contact information to output like in the following example: input:\n    SICK\n    Bernd Hotze\n    Manager Marketing & Sales SICK AG\n S   New Markets\n    Erwin-Sick-Strasse 1\n    79183 Waldkirch, Germany\n    Phone +49 7681 202-3892\n    Mobile +49 1727626031\n    Fax +49 7681 202-3386\n    E-Mail bernd.hotze@sick.de\n    www.sick.com\n    https://de.linkedin.com/in/bernd-hotze-89b70b1\n  \n'''
    #sentence2  = '''\n{\"first_name\": \"\", \"last_name\": \"\",  \"academic_title\": \"\", \"company_name\": \"\", \"position\": \"\", \"street\": \"\", \"house_number\": \"\", \"adress_detail\": \"\", \"zip\": \"\", \"city\": \"\", \"region\": \"\", \"country\": \"\", \"email\": \"\", \"phone_number\": \"\", \"mobile_phone_number\": \"\", \"fax_number\": \"\", \"web_site\": \"\", \"facebook\": \"\",  \"linkedin\": \"\"}'\n'''
    sentence3 = "I want to extract my input contact information to output like in the following example: input:    SICK    Bernd Hotze   Manager Marketing & Sales SICK AG,  S   New Markets   Erwin-Sick-Strasse 1    79183 Waldkirch, Germany   Phone +49 7681 202-3892    Mobile +49 1727626031 Fax +49 7681 202-3386 E-Mail bernd.hotze@sick.de www.sick.com\\n    https://de.linkedin.com/in/bernd-hotze-89b70b1\nPlease respond outputs as json object with fields like; Output: {\"first_name\": \"Bernd\", \"last_name\": \"Hotze\",  \"academic_title\": \"\", \"company_name\": \"SICK AG\", \"position\": \"Manager Marketing & Sales\", \"street\": \"Erwin-Sick-Strasse\", \"house_number\": \"1\", \"adress_detail\": \"\", \"zip\": \"79183\", \"city\": \"Waldkirch\", \"region\": \"Baden- Württemberg\", \"country\": \"Germany\", \"email\": \"bernd.hotze@sick.de\", \"phone_number\": \"+49 7681 202-3892\", \"mobile_phone_number\": \"+49 1727626031\", \"fax_number\": \"+49 7681 202-3386\", \"web_site\": \"www.sick.com\", \"facebook\": \"\",  \"linkedin\": \"https://de.linkedin.com/in/bernd-hotze-89b70b1\"}\n Do not complete fields if they are not given in the input text. If there is only one field given, just give output with one field,do not fill blank fields, do it like: input: Musa Ünal, Output: {\"first_name\": \"Musa\", \"last_name\": \"Ünal\"}, or input:  Ersel, Output: { \"first_name\": \"Ersel\"}, please do not add any other information to output except input, Here comes my input contact information:\n"
    sentence4 = '''\nPlease respond outputs as json object with fields like;\n Output: {\"first_name\": \"Bernd\", \"last_name\": \"Hotze\",  \"academic_title\": \"\", \"company_name\": \"SICK AG\", \"position\": \"Manager Marketing & Sales\", \"street\": \"Erwin-Sick-Strasse\", \"house_number\": \"1\", \"adress_detail\": \"\", \"zip\": \"79183\", \"city\": \"Waldkirch\", \"region\": \"Baden- Württemberg\", \"country\": \"Germany\", \"email\": \"bernd.hotze@sick.de\", \"phone_number\": \"+49 7681 202-3892\", \"mobile_phone_number\": \"+49 1727626031\", \"fax_number\": \"+49 7681 202-3386\", \"web_site\": \"www.sick.com\", \"facebook\": \"\",  \"linkedin\": \"https://de.linkedin.com/in/bernd-hotze-89b70b1\"}\n: '''
    sentence0 = "Output:"
    sentence5 = "I want to extract my input contact information to output like in the following example: input:    SICK    Bernd Hotze   Manager Marketing & Sales SICK AG,  S   New Markets   Erwin-Sick-Strasse 1    79183 Waldkirch, Germany   Phone +49 7681 202-3892    Mobile +49 1727626031 Fax +49 7681 202-3386 E-Mail bernd.hotze@sick.de www.sick.com\\n    https://de.linkedin.com/in/bernd-hotze-89b70b1; Output: {\\\"first_name\\\": \\\"Bernd\\\", \\\"last_name\\\": \\\"Hotze\\\",  \\\"academic_title\\\": \\\"\\\", \\\"company_name\\\": \\\"SICK AG\\\", \\\"position\\\": \\\"Manager Marketing & Sales\\\", \\\"street\\\": \\\"Erwin-Sick-Strasse\\\", \\\"house_number\\\": \\\"1\\\", \\\"adress_detail\\\": \\\"\\\", \\\"zip\\\": \\\"79183\\\", \\\"city\\\": \\\"Waldkirch\\\", \\\"region\\\": \\\"Baden- Württemberg\\\", \\\"country\\\": \\\"Germany\\\", \\\"email\\\": \\\"bernd.hotze@sick.de\\\", \\\"phone_number\\\": \\\"+49 7681 202-3892\\\", \\\"mobile_phone_number\\\": \\\"+49 1727626031\\\", \\\"fax_number\\\": \\\"+49 7681 202-3386\\\", \\\"web_site\\\": \\\"www.sick.com\\\", \\\"facebook\\\": \\\"\\\",  \\\"linkedin\\\": \\\"https://de.linkedin.com/in/bernd-hotze-89b70b1\\\"},  Do not complete fields if they are not given in the input text. If there is only one field given, just give output with one field,do not fill blank fields, do it like: input: Musa Ünal, Output: {\\\"first_name\\\": \\\"Musa\\\", \\\"last_name\\\": \\\"Ünal\\\"}, or input:  Ersel, Output: { \\\"first_name\\\": \\\"Ersel\\\"}, please do not add any other information to output except input, Here comes my input contact information:"
    #complete_prompt = str(sentence1)  +  str(sentence4) + str(sentence5)
    #str(sentence4)+ #str(sentence3)#str(contacts)
    if len(prompt)==0:
        response = openai.Completion.create( model="text-davinci-003", prompt=sentence3 + input + sentence0, temperature=0.7, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0)
    else :
        response = openai.Completion.create( model="text-davinci-003", prompt=prompt + input, temperature=0.7, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0)
    completion = response["choices"][0]["text"]
    return completion
    
def contact_index(request):
    all_contact_texts = ContactText.objects.all().order_by("id").reverse()
    context = {
        'all_contact_texts': all_contact_texts
    }
    #return JsonResponse(all_contact_texts, safe=False)
    return render(request, 'contact_index.html', context)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactText.objects.all().order_by('first_name')
    serializer_class = ContactTextSerializer
    
# class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
#     def get_default_renderer(self, view):
#         return JSONRenderer()

    
@csrf_exempt
def process_json_object(request):
    if request.method=='POST':
        json_object = json.loads(request.body)
        print(json_object)
        contact = ContactText()
        input_text = json_object['input_text']
        
            
        
        contact_dict = {'first_name': '', 'last_name': '', 'academic_title': '', 'company_name': '', 'position': '', 'street': '', 'house_number': '', 'adress_detail': '',
                        'zip': '', 'city': '', 'region': '', 'country': '', 'email': '', 'phone_number': '', 'mobile_phone_number': '', 'fax_number': '', 'web_site': '',
                        'facebook': '', 'linkedin': ''}
        
        result = api_call(input_text)
        tuples = re.findall(r'\{.*\}', result)
        print(tuples)
        output_json = json.dumps(tuples[0])
        output_dict = json.loads(tuples[0])
        contact.output_text = output_json
        contact.first_name = output_dict.get('first_name', '')
        contact.last_name = output_dict.get('last_name', '')
        contact.academic_title = output_dict.get('academic_title', '')
        contact.company_name = output_dict.get('company_name', '')
        contact.position = output_dict.get('position', '')
        contact.street = output_dict.get('street', '')
        contact.house_number = output_dict.get('house_number', '')
        contact.adress_detail = output_dict.get('adress_detail', '')
        contact.zip = output_dict.get('zip', '')
        contact.city = output_dict.get('city', '')
        contact.region = output_dict.get('region', '')
        contact.country = output_dict.get('country', '')
        contact.email = output_dict.get('email', '')
        contact.phone_number = output_dict.get('phone_number', '')
        contact.mobile_phone_number = output_dict.get('mobile_phone_number', '')
        contact.fax_number = output_dict.get('fax_number', '')
        contact.web_site = output_dict.get('web_site', '')
        contact.facebook = output_dict.get('facebook', '')
        contact.linkedin = output_dict.get('linkedin', '')
        contact.save()
        return JsonResponse(output_dict)
    return JsonResponse({'error' : 'use curl to post input_text via mobile phone'})
    
def search_in_pdf(request):
         

    return

def home(request):
    all_contact_texts = ContactText.objects.all().order_by("-id")
    context = context = {'all_contact_texts': all_contact_texts}
    if 'Add' in request.POST:
        contact = ContactText()
        contact.input_text = request.POST.get("Contact")
        #import pdb;pdb.set_trace()
        result = api_call(contact.input_text)
        tuples = re.findall(r'\{.*\}', result)
        output_json = json.dumps(tuples[0])
        output_dict = json.loads(tuples[0])
        contact.output_text = output_json
        contact.first_name = output_dict.get('first_name', '')
        contact.last_name = output_dict.get('last_name', '')
        contact.academic_title = output_dict.get('academic_title', '')
        contact.company_name = output_dict.get('company_name', '')
        contact.position = output_dict.get('position', '')
        contact.street = output_dict.get('street', '')
        contact.house_number = output_dict.get('house_number', '')
        contact.adress_detail = output_dict.get('adress_detail', '')
        contact.zip = output_dict.get('zip', '')
        contact.city = output_dict.get('city', '')
        contact.region = output_dict.get('region', '')
        contact.country = output_dict.get('country', '')
        contact.email = output_dict.get('email', '')
        contact.phone_number = output_dict.get('phone_number', '')
        contact.mobile_phone_number = output_dict.get('mobile_phone_number', '')
        contact.fax_number = output_dict.get('fax_number', '')
        contact.web_site = output_dict.get('web_site', '')
        contact.facebook = output_dict.get('facebook', '')
        contact.linkedin = output_dict.get('linkedin', '')
        contact.save()
        messages.info( request, 'You have successfully saved your ContactText.') 
             
    return render(request, 'button.html', context)
