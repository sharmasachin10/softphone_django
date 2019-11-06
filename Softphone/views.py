from django.shortcuts import render
import plivo
from .plivo_creds import *
from django.views.decorators.csrf import csrf_exempt 

##############################################FUNCTIONS##################################################
#Home
def index(request):
    return render(request, "index.html", {})

#Make Call
def make_call(request):
    to_number = request.POST.get("call_number")
    client = plivo.RestClient(auth_id=auth_id, auth_token=auth_token)
    call_made = client.calls.create(
        from_=calling_number,
        to_=to_number,
        answer_url=answer_url
    )
    return render(request, "call_progress.html", {})



#Receive Call
@csrf_exempt
def receive_call():
    # Generate a Speak XML with the details of the text to play on the call.
    body = "Hello, you just received your first call"
    r = plivoxml.Response()
    r.addSpeak(body)

    print (r.to_xml())
    return Response(str(r), mimetype='text/xml')