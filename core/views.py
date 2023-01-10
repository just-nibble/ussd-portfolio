from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to Princewill's ussd portfolio \n choose a skill to see projects\n"
            response += "1. Python \n"
            response += "2. Golang \n"
            response += "3. Rust \n"
            response += "4. PHP \n"
            response += "5. END \n"

        elif text == "1":
            response = "CON Select an option to see details\n"
            response += "1. MintEngine \n"
            response += "2. Marketier \n"
            response += "3. GiftCarded \n"
        
        elif text == "1*1":
            response = "END MintEngine is a comprehensive suite of web3 instruments spread \nacross an ecosystem of distributed ledgers.\ncan be accessed at https://mintengine.org"

        elif text == "1*2":
            response = "END Marketier helps students buy and sell items for no charge at all!\ndownload at: \nhttps://play.google.com/store/apps/details?id=com.skylex.schoolmart&gl=US&pli=1"

        elif text == "1*3":
            response = "END Create Giftcards for popular cryptocurrency\ndetails:(pending)"

        elif text == "2":
            response = "CON Select an option to see details\n"
            response += "1. Go-notif \n"
            response += "2. LinuxAuto \n"
        
        elif text == "2*1":
            response = "END Linux utility for displaying notification when clipboard changes\ndetails:\nhttps://github.com/just-nibble/go-notif"

        elif text == "2*2":
            response = "END LinuxAuto is a GUI based linux utility for automating software installs\ndetails:\nhttps://github.com/just-nibble/AutoBash-GUI"

        elif text == "3":
            response = "END No projects yet"

        elif text == "4":
            response = "CON Select an option to see details\n"
            response += "1. EDMS \n"
        
        elif text == "4*1":
            response = "END Used PHP and ElasticSearch to create an index engine for an EDMS.\ndetails:\nProtected by NDA"
        
        elif text == "5":
            response = "END Thanks for visiting"
        
        return HttpResponse(response)

          