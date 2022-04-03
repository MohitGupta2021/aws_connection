# This is a sample Python script.
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json

myMQTTClient = AWSIoTMQTTClient(
    "iot")  # random key, if another connection using the same key is opened the previous one is auto closed by AWS IOT
myMQTTClient.configureEndpoint("a37adcjfwz4n3n-ats.iot.us-east-2.amazonaws.com", 8883)

myMQTTClient.configureCredentials("AmazonRootCA1.pem",
                                  "fc04d9accfe28c9f63616f9d8182730aff04cea5730ad16485a8716815bef08e-private.pem.key",
                                  "fc04d9accfe28c9f63616f9d8182730aff04cea5730ad16485a8716815bef08e-certificate.pem.crt")

myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
print('Initiating Realtime Data Transfer From Raspberry Pi...')
myMQTTClient.connect()


def loop():
    while True:
        msg = "Sample data from the device";
        topic = "general/inbound"
        myMQTTClient.publish(topic, msg, 0)
        print("Message Sent")


if __name__ == '__main__':
    try:

        loop()
    except KeyboardInterrupt:
        pass