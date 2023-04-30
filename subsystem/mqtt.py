import paho.mqtt.client as mqtt
from django.conf import settings

from .models import Sensor, SensorLog

def on_message_mqtt(sensor_name):
    def template(client, userdata, msg):
        sen = Sensor.objects.get(name=sensor_name)
        sen.value = msg.payload.decode('utf-8')
        sen.save()
        sen_log = SensorLog(name=sen, value=msg.payload.decode('utf-8'))
        sen_log.save()
    return template

def on_connect(client, userdata, rc, result):
    client.subscribe('waterheating/#')
    client.subscribe('fancontrol/#')
    client.subscribe('lighting/#')

on_message_watertemp = on_message_mqtt('Water Temperature')
on_message_waterrate = on_message_mqtt('Water Usage Rate')
on_message_outtemp = on_message_mqtt('Outside Temperature')

on_message_roomtemp = on_message_mqtt('Room Temperature')
on_message_roomhum = on_message_mqtt('Room Humidity')
on_message_roomco2 = on_message_mqtt('Room CO2')

on_message_light = on_message_mqtt('Light Level')
on_message_occupants = on_message_mqtt('Occupancy')
on_message_daylight = on_message_mqtt('Daylight')

client = mqtt.Client()

client.message_callback_add('waterheating/watertemp', on_message_watertemp)
client.message_callback_add('waterheating/waterusagerate', on_message_waterrate)
client.message_callback_add('waterheating/outtemp', on_message_outtemp)

client.message_callback_add('fancontrol/temp', on_message_roomtemp)
client.message_callback_add('fancontrol/hum', on_message_roomhum)
client.message_callback_add('fancontrol/co2', on_message_roomco2)

client.message_callback_add('lighting/light', on_message_light)
client.message_callback_add('lighting/occupants', on_message_occupants)
client.message_callback_add('lighting/daylight', on_message_daylight)

client.on_connect = on_connect

client.connect(settings.MQTT_HOST, settings.MQTT_PORT)
