import paho.mqtt.client as paho
import DataBase
import DataAnalysis
import os


from dotenv import load_dotenv
load_dotenv()

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def on_subscribe(client, userdata, mid, granted_qos):
    #print("Subscribed: " + str(mid) + " " + str(granted_qos))
    pass


def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    dbObject = DataBase.DataBase()
    dbObject.writeData(msg.pDDayload)


def on_connect(client, userdata, flags, rc):
    #print("Connected with result code "+str(rc))
    client.subscribe("sensornode/livestream/LightIntensity/x", qos=1)


client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_connect = on_connect

client.connect(os.getenv("BROKER_ADDRESS"), int(os.getenv("BROKER_PORT")))
client.loop_start()

while True:
    val = input("Press Q for quit, D for delete DataBase, V for visualize")
    if val == "Q":
        client.loop_stop(force=False)
        print("Stopped the client")
        break
    elif val == "D":
        dbObject = DataBase.DataBase()
        dbObject.clearTable()
        print("Deleted all the recorded Data")
    elif val == "V":
        DataAnalysis.plotGraph()


