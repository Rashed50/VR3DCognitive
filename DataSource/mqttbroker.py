import paho.mqtt.client as mqtt
from django.conf import settings
from django.db import connection
import logging,json,random,time,datetime
from DataSource.models import VRModel
#from APIApp.IncomingData import IncomingData


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        # print('=============================== Connected successfully =============================================')
        mqtt_client.subscribe('vrsensors')
    else:
        print('Bad connection. Code:', rc)


def on_message(mqtt_client, userdata, msg):
   
    #IncomingData.storeIncomingData(msg.topic,msg.payload)
    
    print(f'\n 1.Received message on_message() ====== {msg} ')
    storeIncomingData(msg.topic,msg.payload)


def createDemoData(mdel:VRModel):
    vrmod = VRModel()
    return vrmod
    

def storeIncomingData(topic,payload): 
    payload = json.loads(payload) # extraction json     
    print(f'\n 2.Received message on_message() ====== topic: {topic} with payload:{payload} ')

    session_id = payload['session_id'] # random.randrange(1111,9999)
    frame_number = payload['frame_number'] # random.randrange(99999,999999)
    timestamp = payload['timestamp'] # time.time()
    msg = payload['msg']

    sensor_data = {
    "incoming_message":msg,
    "HeadUserPresence": False,
    "HeadIsTracked": False,
    "HeadTrackingState": 0,
    "HeadDevicePosition": "(0.00, 0.00, 0.00)"
    }
    # convert into JSON:
    #sensor_data = json.dumps(sensor_data)
    data =VRModel(sessionId=session_id,frameNumber=frame_number,topic=topic,message=msg) #  VRModel(sessionID= session_id,frame_number=frame_number,timestamp= timestamp,topic=topic,message= msg)
    data.save()


#def startMQttBroker():
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message 
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
#client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)
client.loop_start()
    
    
  