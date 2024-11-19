from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json, random,time
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import VRUser,VRModel
#from DataSource.mqttt import mqttt as mqtt_client2
# mqtt file import
from VR3DCognitive.mqtt import client as mqtt_client
 


def index(request):
        
   # template = loader.get_template('index.html')
   # return HttpResponse("hello");
   # return HttpResponse(template.render())
   my_name = "Hasan"
   info = {'name':my_name}
   return render(request,'public/index.html',info)

def signup(request):
    template = loader.get_template('signup_form.html')
    return HttpResponse(template.render())

@csrf_exempt
def createNewMember(request):
    if(request.method == 'POST'):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        password = request.POST.get('password')
        country_id = request.POST.get('country_id')
        state_id = request.POST.get('state_id')
        city = request.POST.get('city')
        address = request.POST.get('address')
        address2 = request.POST.get('address2')
        zip = request.POST.get('zip')
        user = VRUser(first_name=first_name,last_name=last_name,contact_no=contact_no,email=email,password=password,country_id=1,state_id=1,city="",address=address,address2="",zip=zip)
        user.save()
        return HttpResponse("Successfully Saved")


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())



def sendMessage(request):

    x =  '{ "topic":"django/mqtt", "msg":"================ This is test message ======================="}'
    request_data =  json.loads(x)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    print('=========================== Message Sent =======================================');
    session_id =  random.randrange(1111,9999)
    frame_number = random.randrange(99999,999999)
    timestamp = time.time()

    sensor_data = {
        "HeadUserPresence": "False",
        "HeadIsTracked": "False",
        "HeadTrackingState": "0",
        "HeadDevicePosition": "(0.00, 0.00, 0.00)"
    }

    # convert into JSON:
    sensor_data = json.dumps(x)

    data = VRModel(sessionID= session_id,frame_number=frame_number,timestamp= timestamp,sensor_data=sensor_data)
    data.save() 

    return JsonResponse({'code': rc,'message':'Successfully send'})



