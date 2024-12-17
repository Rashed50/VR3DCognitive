import paho.mqtt.client as mqtt
from django.conf import settings
from django.db import connection
import logging,json,random,time,datetime
from DataSource.models import VRModel
import ssl


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        # print('=============================== Connected successfully =============================================')
        mqtt_client.subscribe('vrsensors')
    else:
        print('Bad connection. Code:', rc)

# def on_message(client, userdata, message, properties=None):
#     print(" ===========Received message " + str(message.payload)  + " on topic '" + message.topic + "' with QoS " + str(message.qos))

def on_message(mqtt_client, userdata, msg):
       
    print(f'\n 1.Received message on_message() ====== {msg} ')
    storeIncomingData(msg.topic,msg.payload)


def storeIncomingData(topic,payload): 
    payload = json.loads(payload) # extraction json     
    print(f'\n 2.Received message for storing in database ====== topic: {topic} with payload:{payload} ')

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
#client.subscribe("vrsensor",qos=2)
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
#client.username_pw_set('','')
#client.tls_insecure_set(False)
#client.connect_async(host=settings.MQTT_SERVER)
#client.tls_set()
client.tls_set(certfile=None,
               keyfile=None,
               cert_reqs=ssl.CERT_REQUIRED)

connection_status = client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE,
   # clean_start=mqtt.MQTT_CLEAN_START_FIRST_ONLY,
)
print(f"connecting to MQTT broker- version {client.callback_api_version}------------------- user= {settings.MQTT_USER} status  {connection_status}")
client.loop_start()
    
    
  