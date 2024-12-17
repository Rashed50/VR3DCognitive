import json, random, time
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.views import View, generic
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.urls import reverse, reverse_lazy

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#from DataSource.mqttt import mqttt as mqtt_client2
# mqtt file import
#from VR3DCognitive.mqtt import client as mqtt_client    
from DataSource.mqttbroker import client as mqtt_client
# from DataSource.ssl_mqtt import client as mqtt_ssl_client


## Custom Import
from DataSource.models import Country, VRUser, VRModel
from DataSource.serializers import CountrySerializer

User = get_user_model()





class Home(generic.TemplateView):
    template_name = 'layouts/master.html'

    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        
        context['banner_show'] = True
        context['info'] = {
            'name': ''
        }
        return context




class SignupView(View):
    template_name = "auth/signup.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('f_name')
        last_name  = request.POST.get('l_name')
        email      = request.POST.get('email')
        phone      = request.POST.get('phone')
        country    = request.POST.get('country')
        city       = request.POST.get('city')
        address    = request.POST.get('address')
        password   = request.POST.get('password')
        confirm_password = request.POST.get('c_password')

        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, self.template_name, {
                'first_name': first_name,
                'last_name' : last_name,
                'email'     : email,
                'phone'     : phone,
                'country'   : country,
                'city'      : city,
                'address'   : address
            })

        try:
            username = email.split('@')[0]

            if User.objects.filter(username=username).exists():
                username = f"{username}{User.objects.filter(username__startswith=username).count() + 1}"

            user = User.objects.create(
                username   = username,
                first_name = first_name,
                last_name  = last_name,
                email      = email,
                password   = make_password(password) 
            )

            try:
                country_obj = Country.objects.get(id=int(country))
            except Country.DoesNotExist:
                messages.error(request, "Invalid country selected.")
                return render(request, self.template_name)

            existing_vr_user = VRUser.objects.filter(user_id=user).first()

            if existing_vr_user:
                existing_vr_user.contact_no = phone
                existing_vr_user.country_id = country_obj
                existing_vr_user.city       = city
                existing_vr_user.address    = address
                existing_vr_user.save()
                messages.success(request, "Your account has been created successfully! Please log in.")
            else:
                vr_user = VRUser.objects.create(
                    user_id    = user,
                    contact_no = phone,
                    country_id = country_obj,
                    city       = city,
                    address    = address
                )
                messages.success(request, "Account created successfully! Please log in.")

            return redirect('login_form')  

        except Exception as e:
            messages.error(request, f"Error: {e}")
            return render(request, self.template_name)



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
                return redirect('admin_dashboard')  
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
    


def sendMessage(request):

    session_id =  random.randrange(1111,9999)
    frame_number = random.randrange(99999,999999)
    timestamp = time.time()
       
    topic = "vrsensors"
    payload = '{ "msg":"Message Receiving from web Application", "session_id":"654654132","frame_number":"741852963","timestamp":"898986565232" }  '

    #request_data =  json.loads(payload)
    rc, mid = mqtt_client.publish(topic, payload)
    print('=========================== Message Sent =======================================')


    sensor_data = {

        "HeadUserPresence": False,
        "HeadIsTracked": False,
        "HeadTrackingState": 0,
        "HeadDevicePosition": "(0.00, 0.00, 0.00)"
    }
    # convert into JSON:
    sensor_data = json.dumps(sensor_data)
    return JsonResponse({'status code': rc,'message': 'Successfully send and save in database','message_id':mid })



## API's
    """
    API view to retrieve a list of all countries.
    """





## Admin Views -----------------------------
class AdminHomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'admin_dashboard/home.html'
    login_url = reverse_lazy('login_form')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active']          = 'admin_home'
        context['total_users']     = User.objects.all().count()
        context['total_countries'] = Country.objects.all().count()
        context['total_models']    = VRModel.objects.all().count()
        return context




class VRModelListView(LoginRequiredMixin, generic.ListView):
    model = VRModel  
    template_name = 'admin_dashboard/vr3d/vr_model_list.html'  
    context_object_name = 'vr_models'    
    paginate_by = 10  
    login_url = reverse_lazy('login_form')
    
    def get_context_data(self, **kwargs):
        context = super(VRModelListView, self).get_context_data(**kwargs)
        context['active']       = 'vr_list'
        context['total_models'] = VRModel.objects.all().count()
        return context
    





## API's Views -----------------------------
class CountryListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        countries  = Country.objects.all()  
        serializer = CountrySerializer(countries, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)