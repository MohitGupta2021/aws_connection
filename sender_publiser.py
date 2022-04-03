from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import time
import json
from random import uniform
import datetime

# using now() to get current time

myMQTTClient = AWSIoTMQTTClient("things_iot")

myMQTTClient.configureEndpoint("a37adcjfwz4n3n-ats.iot.us-east-2.amazonaws.com", 8883)
myMQTTClient.configureCredentials("AmazonRootCA1.pem","fc04d9accfe28c9f63616f9d8182730aff04cea5730ad16485a8716815bef08e-private.pem.key","fc04d9accfe28c9f63616f9d8182730aff04cea5730ad16485a8716815bef08e-certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1) # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2) # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10) # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5) # 5 sec
print ('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()

print("Client Connected")




def loop():

    while True:
        time.sleep(1000)
        current_time = datetime.datetime.now()
        tempreading = uniform(20.0, 25.0)
        humidityreading = uniform(80.0, 90.0)
        Treading = str(current_time)

        payload = json.dumps({'timestamp': Treading, 'temperature': tempreading, 'humidity': humidityreading}
                             )
        topic = "general"
        myMQTTClient.publish(topic, payload, 0)

        print("Message Sent")
        print(current_time)


if __name__ == '__main__':
    try:

        loop()
        time.sleep(1000)
    except KeyboardInterrupt:
        pass