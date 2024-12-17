import paho.mqtt.client as mqtt
from django.conf import settings
from django.db import connection
import logging,json,random,time,datetime


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        # print('=============================== Connected successfully =============================================')
        mqtt_client.subscribe('vr_sensor3')
    else:
        print('Bad connection. Code:', rc)


def on_message(mqtt_client, userdata, msg):
   
    #IncomingData.storeIncomingData(msg.topic,msg.payload)
  #  print(f'\nReceived message on_message() ====== topic: {msg.topic} with payload:{msg.payload} ')
     storeIncomingData(msg.topic,msg.payload)



def storeIncomingData(topic,payload):     
    print(f'\nReceived message on_message() ====== topic: {topic} with payload:{payload} {datetime.date.today()}')

    session_id =  random.randrange(1111,9999)
    frame_number = random.randrange(99999,999999)
    timestamp = time.time()

    sensor_data = {
    "HeadUserPresence": False,
    "HeadIsTracked": False,
    "HeadTrackingState": 0,
    "HeadDevicePosition": "(0.00, 0.00, 0.00)"
    }
    # convert into JSON:
    sensor_data = json.dumps(sensor_data)
    #data = VRModel(sessionID= session_id,frame_number=frame_number,timestamp= timestamp,sensor_data=sensor_data)
    #data.save()


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






