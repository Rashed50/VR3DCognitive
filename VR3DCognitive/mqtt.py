import paho.mqtt.client as mqtt
from django.conf import settings
import logging


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('=============================== Connected successfully =============================================')
        mqtt_client.subscribe('vr3d')
    else:
        print('Bad connection. Code:', rc)


def on_message(mqtt_client, userdata, msg):
    print(f'Received message on ====== topic: {msg.topic} with payload: {msg.payload}')


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
