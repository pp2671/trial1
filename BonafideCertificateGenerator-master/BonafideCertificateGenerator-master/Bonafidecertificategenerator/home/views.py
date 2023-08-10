from instamojo_wrapper import Instamojo
from django.shortcuts import render
from home.models import Submit
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import FileResponse
from PIL import Image,ImageDraw,ImageFont
import img2pdf 
from django.contrib import messages
import json
#from django.views.decorators.csrf import csrf_exempt
from django. conf import settings
import requests
from rest_framework.response import Response
import random
import string

import os
# Create your views here.


def index(request):
    #API_KEY = "344a5f7f5e294e344343d39f7dc51d19"
    #AUTH_TOKEN = "e9b6ebf86a182545a23254674757dea6" 
    API_KEY = "test_3cdf105871d434dde9223e334f9"
    AUTH_TOKEN = "test_3d87a43706a9d366078620af461"

    if request.method == "POST":
        Name = request.POST['Name']
        year = request.POST['Year']
        course = request.POST['Course']
        division = request.POST['Division']
        rollno = request.POST['Rollno']
        gender = request.POST['Gender']
        Enroll = request.POST['EnrollNo']
        Email = request.POST['Email']
        year2=""
        

        
        if course=="MCA" :
            course2="MC"
        elif course=="MBA":
            course2="MBA"
        elif course=="Engineering":
            course2="Engg"
        else :
            course2="EE"  

        if year=="First Year" :
            year2="FY"
        elif year=="Second Year" :
            year2="SY"
        elif year == "Third Year":
            year3 = "TY"
        else:
            year2="LY"
        
         

        classname=year2+course2+division


        

        if Submit.objects.raw("SELECT * FROM home_submit WHERE Enroll== %s AND Name==%s AND Year==%s AND Course==%s AND Gender==%s AND Rollno==%s AND Division==%s" ,[Enroll,Name,year,course,gender,rollno,division]):    
            img = Image.open(r'C:\Users\prana\OneDrive\Desktop\BonafideCertificateGenerator-master\BonafideCertificateGenerator-master\Bonafidecertificategenerator\home\static\home\template.png')
            # Convert to RGB mode
            if img.mode != "RGB":
                img = img.convert("RGB")    
            draw = ImageDraw.Draw(img)
            draw = ImageDraw.Draw(img)      
            font = ImageFont.truetype('arial.ttf',30)
            font2 = ImageFont.truetype('arial.ttf',30)

            draw.text(xy=(458,310,1065,327),text=Name,fill=(0,0,0),font=font)
            draw.text(xy=(320,395,433,413),text=classname,fill=(0,0,0),font=font2)
            draw.text(xy=(617,397,727,410),text=rollno,fill=(0,0,0),font=font)
            draw.text(xy=(1039,397,1258,407),text=Enroll,fill=(0,0,0),font=font)


            img.save(r"C:\Users\prana\OneDrive\Desktop\BonafideCertificateGenerator-master\BonafideCertificateGenerator-master\Bonafidecertificategenerator\home\certificates\{}.png".format(Enroll))
            # storing image path 
            img_path = r"C:\Users\prana\OneDrive\Desktop\BonafideCertificateGenerator-master\BonafideCertificateGenerator-master\Bonafidecertificategenerator\home\certificates\{}.png".format(Enroll)

            # storing pdf path 
            pdf_path = (r"C:\Users\prana\OneDrive\Desktop\BonafideCertificateGenerator-master\BonafideCertificateGenerator-master\Bonafidecertificategenerator\home\certificates\{}.pdf".format(Enroll))
            
            # opening image 
            image = Image.open(img_path) 
            
            # converting into chunks using img2pdf 
            pdf_bytes = img2pdf.convert(image.filename) 

            # opening or creating pdf file
            file = open(pdf_path, "wb") 
            
            # writing pdf files with chunks 
            file.write(pdf_bytes) 
            
            # closing image file 
            image.close() 
            
            # closing pdf file
            file.close()
            
        
            pdf = open(r"C:\Users\prana\OneDrive\Desktop\BonafideCertificateGenerator-master\BonafideCertificateGenerator-master\Bonafidecertificategenerator\home\certificates\{}.pdf".format(Enroll),'rb')
            os.remove(r"C:\Users\prana\OneDrive\Desktop\BonafideCertificateGenerator-master\BonafideCertificateGenerator-master\Bonafidecertificategenerator\home\certificates\{}.png".format(Enroll))
            location = r"C:\Users\prana\OneDrive\Desktop\BonafideCertificateGenerator-master\BonafideCertificateGenerator-master\Bonafidecertificategenerator\home\certificates\{}.pdf".format(Enroll),'rb'
            #return pay(Enroll)
            #url = "http://localhost:8000/E:/Bonafidecertificategenerator/Bonafidecertificategenerator/home/certificates/{}.pdf".format(Enroll)
            api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN , endpoint='https://test.instamojo.com/api/1.1/')

            # Create a new Payment Request
            url = ("http://localhost:8000/home/{}".format(Enroll))

            # response = api.payment_request_create(
            #     amount='50',
            #     purpose='Fee for Bonafided Certificate',
            #     send_email=True,
            #     email=Email,
            #     redirect_url=url
            #     )
                
            # print the long URL of the payment request.
            # url = response['payment_request']['longurl']
          
          
            # print the unique ID(or payment request ID)
            return HttpResponseRedirect(url)
            
            #return FileResponse(pdf)
            
                   
        else:
           return HttpResponse("Student not found")
   
    return render(request, "home/index.html")

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    

def file(request,file):
    pdf = open(r"C:\Users\prana\OneDrive\Desktop\BonafideCertificateGenerator-master\BonafideCertificateGenerator-master\Bonafidecertificategenerator\home\certificates\{}.pdf".format(file),'rb')
    return FileResponse(pdf)
   
    
               
                
                
                    
            

            

    



