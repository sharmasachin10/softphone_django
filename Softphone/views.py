from django.shortcuts import render
import plivo
from plivo import plivoxml
from .plivo_creds import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import redirect 



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
    print("call_made----------------",call_made)
    return render(request, "call_progress.html", {})



#Receive Call
@csrf_exempt
def receive_call(request):
    # Generate a Speak XML with the details of the text to play on the call.
    response = plivoxml.ResponseElement()
    response.add(plivoxml.PlayElement('/home/Softphone/softphone_django/static/audio/ring.mp3'))
    print(response.to_string())
    body = "Hello, you just received your first call"
    r = plivoxml.ResponseElement()
    r.add_speak(body)

    print (r.to_string())
    #return HttpResponse(str(r))
    return redirect("/")


#Receive Call
@csrf_exempt
def hangup_call(request):
    print("hangup_call----------------",request)
    