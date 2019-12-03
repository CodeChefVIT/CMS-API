from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Details
from rest_framework.decorators import api_view
from .serializers import DetailsSerializer
import pyqrcode
from PIL import Image
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import png

@csrf_exempt
@api_view(['GET', 'POST'])
def details_view(request):

    if request.method == 'GET':
        snippets = Details.objects.all()
        serializer = DetailsSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            rfid = serializer.data['rfid']
            email = serializer.data['email']
            url = pyqrcode.create(rfid) 
            
            # Create and save the png file naming "myqr.png" 
            url.png('static/'+rfid+'.png', scale = 8) 
            subject, from_email, to = 'hello', 'rayanuthalas@gmail.com', email
            text_content = 'This is an important message from CodeChef-VIT. Please use this QR Code for further Events.'
            html_content = '<p>This is an <strong>important</strong> message from <b>CodeCheff-VIT.</b> Please use this QR Code for further Events.</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.attach_file('static/'+rfid+'.png')
            msg.send()
            return JsonResponse("Added Succesfuly",safe=False, status=201)
        return JsonResponse(serializer.errors, status=400)

    