import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
def customCallback(client,userdata,message):
    print("callback came...")
    print(message.payload)

myMQTTClient = AWSIoTMQTTClient("things_iot")

myMQTTClient.configureEndpoint("ats.iot.us-east-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("AmazonRootCA1.pem","fc04d9accfe28c9f63616f9d8182730aff04cea5730ad16485a8716815bef08e-private.pem.key","fc04d9accfe28c9f63616f9d8182730aff04cea5730ad16485a8716815bef08e-certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec

myMQTTClient.connect()
print("Client Connected")

myMQTTClient.subscribe("general", 1, customCallback)
print('waiting for the callback. Click to conntinue...')
x = input()

myMQTTClient.unsubscribe("general")
print("Client unsubscribed")


myMQTTClient.disconnect()
print("Client Disconnected")
