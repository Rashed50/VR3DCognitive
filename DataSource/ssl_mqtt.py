#!/usr/bin/env python

import paho.mqtt.client as mqtt
import os
import ssl
import time
import inspect
from django.conf import settings



def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client()
client.tls_set(
    certfile=r"E:\\My_Work\\VR3DCognitive\\MqttData\\vr.crt",
    # ca_certs=r"D:\\Texon\\21-10-2024\\3d\\VR3DCognitive\\MqttData\\fullchain.pem",
    # keyfile=r"D:\\Texon\\21-10-2024\\3d\\VR3DCognitive\\MqttData\\privateKey.key"
)
client.tls_insecure_set(True)
client.on_connect = on_connect
client.connect(settings.MQTT_SERVER, settings.MQTT_PORT_8084, 60)

client.loop_forever()


## Commend for check connection 
"""
openssl x509 -noout -modulus -in "D:\\Texon\\21-10-2024\\3d\\VR3DCognitive\\MqttData\\vr.crt"
openssl rsa -noout -modulus -in "D:\\Texon\\21-10-2024\\3d\\VR3DCognitive\\MqttData\\privateKey.key"

openssl verify -CAfile [path_to_ca_bundle.pem] "D:\\Texon\\21-10-2024\\3d\\VR3DCognitive\\MqttData\\vr.crt"
openssl verify -CAfile "C:\\Users\\Texon\\fullchain.pem" "D:\\Texon\\21-10-2024\\3d\\VR3DCognitive\\MqttData\\vr.crt"
"""



# Change to the project root directory
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
# os.chdir(project_root)

# # MQTT broker configuration
# broker_address = "mgbckr.net"  # This must match the CN in your server certificate
# port = 8883  # Secure MQTT port
# topic = "T/GettingStarted/pubsub"

# # Certificate paths
# ca_cert_path = os.path.join(settings.BASE_DIR, 'MqttData', 'fullchain.pem')
# client_cert_path = os.path.join(settings.BASE_DIR, 'MqttData', 'vr.crt')
# client_key_path = os.path.join(settings.BASE_DIR, 'MqttData', 'privateKey.key')

# # Print resolved paths
# print(" ++++++++++++++ Resolved Paths: ++++++++++++++")
# print("CA Cert Path:", ca_cert_path)
# print("Client Cert Path:", client_cert_path)
# print("Client Key Path:", client_key_path)

# # Check if certificate files exist
# if not os.path.exists(ca_cert_path):
#     raise FileNotFoundError(f"CA Certificate not found: {ca_cert_path}")
# if not os.path.exists(client_cert_path):
#     raise FileNotFoundError(f"Client Certificate not found: {client_cert_path}")
# if not os.path.exists(client_key_path):
#     raise FileNotFoundError(f"Client Key not found: {client_key_path}")

# # SSL Configuration
# ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# ssl_context.verify_mode = ssl.CERT_REQUIRED
# # ssl_context.load_verify_locations(cafile=ca_cert_path)
# # ssl_context.load_cert_chain(certfile=client_cert_path, keyfile=client_key_path)

# ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
# ssl_context.load_verify_locations(cafile="D:/Texon/21-10-2024/3d/VR3DCognitive/MqttData/fullchain.pem")
# ssl_context.load_cert_chain(certfile=client_cert_path, keyfile=client_key_path)





# # Callback for message reception
# def on_message(client, userdata, message):
#     print(
#         f"Received message: {message.payload.decode('utf-8')} "
#         f"on topic: {message.topic} with QoS: {message.qos} retain: {message.retain}"
#     )

# # Initialize MQTT client
# client = mqtt.Client()

# # Attach callbacks
# client.on_message = on_message

# # Set up SSL/TLS
# client.tls_set_context(ssl_context)

# # Set username and password for authentication (if required)
# client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)

# # Connect to the MQTT broker
# print("Connecting to broker...")
# client.connect(broker_address, port, keepalive=60)

# # Start the network loop
# client.loop_start()

# # Subscribe to the topic
# print(f"Subscribing to topic: {topic}")
# client.subscribe(topic)

# # Publish messages
# for i in range(1, 10):
#     message = f"Hello world from MQTT {i}"
#     print(f"Publishing message: {message}")
#     client.publish(topic, message)
#     time.sleep(1)

# # Stop the network loop
# client.loop_stop()

# print("Goodbye!")
