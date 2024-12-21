#!/usr/bin/env python
import paho.mqtt.client as mqtt
import ssl, time, inspect, os
from django.conf import settings


# Make sure we're running from project-root regardless where this was invoked from
scriptdir = os.path.dirname( os.path.abspath(inspect.getfile(inspect.currentframe())) )
os.chdir( scriptdir )
os.chdir( '../../..' )
print( 'WDIR: ' + os.path.abspath("vr.crt") )


broker_address="mgbckr.net" # this must match the CNAME in your server-cert!
topic="T/GettingStarted/pubsub"

CA_CERT_PATH = "E:\My_Work\VR3DCognitive\DataSource\fullchain.pem"  # Certificate Authority file
CLIENT_CERT_PATH = "E:\My_Work\VR3DCognitive\DataSource\vr.crt"    # Optional, client certificate
CLIENT_KEY_PATH = "DataSource/privateKey.key"  # Optional, client key


def on_message(client, userdata, message):
     print(" ===========Received message " + str(message.payload)  + " on topic '" + message.topic + "' with QoS " + str(message.qos) + " retain " + str(message.retain))
    # print("message received "  + str(message.payload.decode("utf-8"))
    # print ("message topic="      , message.topic)
    # print ("message qos="        , message.qos)
    # print ("message retain flag=", message.retain) E:\My_Work\VR3DCognitive\DataSource\myssl.crt


 
client = mqtt.Client()

print( "connecting to broker" )
#client.tls_set("myssl.pem", "myssl.crt", "myssl.key", tls_version=ssl.PROTOCOL_TLSv1_2)
sslSettings  = ssl.SSLContext()
sslSettings.verify_mode  = ssl.CERT_REQUIRED
sslSettings.load_verify_locations(cafile=CLIENT_CERT_PATH)
#sslSettings.load_cert_chain(certfile=CLIENT_CERT_PATH)
client.tls_set(
    ca_certs= CLIENT_CERT_PATH,              # CA certificate file
    #certfile=CLIENT_CERT_PATH,         # Client certificate file (optional)
    #keyfile=CLIENT_KEY_PATH,           # Client private key file (optional)
    #tls_version=ssl.PROTOCOL_TLSv1_2   # TLS version
)
#client.tls_insecure_set(True)
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect( broker_address, 8084, 60 )

client.loop_start()

print( "Subscribing to topic", topic )
client.on_message=on_message
client.subscribe( topic )

for i in range( 1, 10 ):
    print( "Publishing message to topic" , topic )
    client.publish( topic, "Hello world from MQTT "+str(i) )
    time.sleep( 1 )

client.loop_stop()

print( "Goodbye!" )