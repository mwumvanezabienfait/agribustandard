from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def  welcome(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='mwumvanezab@gmail.com'
api_key ='9cd32813a0d258ce4fceded4ef097e84c0a878fbc3a883bf68d9149970a119df'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):
    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number = request.POST.get("phoneNumber")
        text = request.POST['text']
        # 1*1*1
        level = text.split('*')
        category = text[:3]
        response = ""
        #  main menu for our application
        if text == '':
            response ="CON Murakoze murisanga kuri agribusiness \n"
            response += "1. Kwandikisha ubutaka \n"
            response += "2. Kwandikisha igihingwa \n"
            response += "3. Kwandikisha umusaruro \n"
        # elif text == '1':
        #     response = "CON Hitamo akarere \n"
        #     response += "1.rubavu \n"
        #     response += "2.nyabihu\n"
        #     response += "3.musanze\n"
        # elif text == '1*1':
        #     response = "CON uzuza umwirondoro\n"
        #     response += "numero yirangamuntu\n"
        #
        # elif text == '1*1*1':
        #     response = "CON Hitamo ubuso bwubutaka\n"
        #     response += "1.hegitare 1-5 \n"
        #     response += "2.hegitare 5-10\n"
        #     response += "3.hegitare zirenze icumi\n"
        # elif text == '1*1*1*1':
        #     response = "END Murakoze ,"
        # elif text == '1*2':
        #     response = "CON uzuza umwirondoro\n"
        #     response += "1.numero yirangamuntu\n"
        # elif text == '1*2*1':
        #     response = "CON Hitamo ubuso bwubutaka\n"
        #     response += "1.hegitare 1-5 \n"
        #     response += "2.hegitare 5-10\n"
        #     response += "3.hegitare zirenze icumi\n"
        # elif text == '1*3':
        #     response = "CON uzuza umwirondoro\n"
        #     response += "1.numero yirangamuntu\n"
        # elif text == '1*3*1':
        #     response = "CON Hitamo ubuso bwubutaka\n"
        #     response += "1.hegitare 1-5 \n"
        #     response += "2.hegitare 5-10\n"
        #     response += "3.hegitare zirenze icumi\n"
        #
        # elif text == '2':
        #     response = "CON shyiramo ubwoko bwigihingwa \n"
        #     response += "1. ibirayi \n"
        #     response += "2. ibishyimbo\n"
        #     response += "3. ibigori\n"
        # elif text == '2*1':
        #     response = "CON Hitamo ubwoko bwimbuto\n"
        #     response += "1.kinigi \n"
        #     response += "2.makoroni\n"
        # elif text == '2*1*1':
        #     response = "END Murakoze "
        # elif text == '2*1*2':
        #     response = "END Murakoze "
        #
        # elif text == '2*2':
        #     response = "CON Hitamo ubwoko bwimbuto\n"
        #     response += "1.umutuku \n"
        #     response += "2.umukara\n"
        # elif text == '2*2*1':
        #     response = "END Murakoze "
        # elif text == '2*2*2':
        #     response = "END Murakoze "
        #
        # elif text == '2*3':
        #     response = "CON Hitamo ubwoko bwimbuto\n"
        #     response += "1.tubura \n"
        #     response += "2.inyarwanda\n"
        # elif text == '2*3*1':
        #     response = "END Murakoze "
        # elif text == '2*3*2':
        #     response = "END Murakoze "
        #
        # elif text == '3':
        #     response = "CON andika umusaruro\n"
        #     response += "1. ibirayi \n"
        #     response += "2. ibishyimbo\n"
        #     response += "3. ibigori\n"
        # elif text == '3*1':
        #     response = "END Murakoze kwandikisha umusaruro"
        # elif text == '3*2':
        #     response = "END Murakoze kwandikisha umusaruro"
        # elif text == '3*3':
        #     response = "END Murakoze kwandikisha umusaruro"

        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')