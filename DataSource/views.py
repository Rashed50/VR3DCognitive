from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json, random, time
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import VRUser,VRModel
#from DataSource.mqttt import mqttt as mqtt_client2
# mqtt file import
from VR3DCognitive.mqtt import client as mqtt_client
from django.views import View, generic
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy



User = get_user_model()


# def index(request):
        
#    # template = loader.get_template('index.html')
#    # return HttpResponse("hello");
#    # return HttpResponse(template.render())
#    my_name = "Hasan"
#    info = {'name':my_name}
#    return render(request,'layouts/master.html',info)


class Home(generic.TemplateView):
    template_name = 'layouts/master.html'

    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        
        context['banner_show'] = True
        context['info'] = {
            'name': ''
        }
        return context



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



# def login(request):
#     return render(request, 'auth/login.html')

class LoginView(View):
    template_name = "auth/login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()

        if user:
            auth_user = authenticate(request, username=user.username, password=password)
            
            if auth_user is not None:
                login(request, auth_user) 
                return redirect('vr_model_list')  
            else:
                messages.error(request, "Incorrect password!")
        else:
            messages.error(request, "Unregistered user!")

        return render(request, self.template_name)



class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login_form') 

    def get(self, request):
        if request.user.is_authenticated:
            logout(request)  
            return redirect('login_form')
        return redirect('index')
    



class VRModelListView(LoginRequiredMixin, generic.ListView):
    model = VRModel
    template_name = 'vr3d/vr_model_list.html'  
    context_object_name = 'vr_models'    
    paginate_by = 10  
    login_url = reverse_lazy('login_form')
    
    def get_context_data(self, **kwargs):
        context = super(VRModelListView, self).get_context_data(**kwargs)
        context['total_models'] = VRModel.objects.all().count()
        return context
    



def sendMessage(request):

    session_id =  random.randrange(1111,9999)
    frame_number = random.randrange(99999,999999)
    timestamp = time.time()
       
    x = '{ "topic":"vr3d", "msg":"================ This is test message ======================="}'
       
    request_data =  json.loads(x)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    print('=========================== Message Sent =======================================')


    sensor_data = {
        "HeadUserPresence": False,
        "HeadIsTracked": False,
        "HeadTrackingState": 0,
        "HeadDevicePosition": "(0.00, 0.00, 0.00)"
    }
    # convert into JSON:
    sensor_data = json.dumps(sensor_data)
    data = VRModel(sessionID= session_id,frame_number=frame_number,timestamp= timestamp,sensor_data=sensor_data)
    data.save() 
    return JsonResponse({'code': rc,'message':'Successfully send and save in database'})



