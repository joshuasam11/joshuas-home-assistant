import time
import json
import random
import paho.mqtt.client as mqtt

student_name = "Joshua S"
unique_id = "42612024"
topic = "home/joshuas-2025/sensor"
BROKER = "localhost"
PORT = 1883

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER,PORT,60)
client.loop_start()
btemp = 25
bhum = 60
bgas = 350

while True:
    temp = btemp + random.uniform(-2, 2)   # 23–27
    hum = bhum + random.uniform(-5, 5)      # 55–65
    gas = bgas + random.randint(-20, 20)   # 330–370
    payload = {
        "temperature": round(temp,1),
        "humidity": round(hum,1),
        "gas_level": gas
    }
    print(f"Publishing to {topic}: {payload}")
    client.publish(topic, json.dumps(payload), retain=True)
    time.sleep(5)
