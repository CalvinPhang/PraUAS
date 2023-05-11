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
    client.subscribe('hewantelur/#')
    client.subscribe('redmeat/#')
    client.subscribe('whitemeat/#')
    client.subscribe('grains/#')
    client.subscribe('veg/#')
    client.subscribe('fruits/#')
    client.subscribe('weather/#')
    client.subscribe('sales/#')
    client.subscribe('customer/#')

on_message_yolkcolor = on_message_mqtt('Yolk Color Hue')
on_message_ammonia = on_message_mqtt('Ammonia')
on_message_bacterial = on_message_mqtt('Dairy Bacterial')

on_message_humidity = on_message_mqtt('Humidity')
on_message_ozone = on_message_mqtt('Ozone')
on_message_gas = on_message_mqtt('Gas')

on_message_fat = on_message_mqtt('NIR Spectroscopy')
on_message_impedance = on_message_mqtt('Impedance')
on_message_ph = on_message_mqtt('pH')

on_message_moisture = on_message_mqtt('Hyperspectral Imaging')
on_message_texture = on_message_mqtt('Acoustic')
on_message_density = on_message_mqtt('Capacitive')

on_message_activity = on_message_mqtt('Chlorophyll Fluorescence')
on_message_ethylene = on_message_mqtt('Ethylene')
on_message_temperature = on_message_mqtt('Temperature')

on_message_weight = on_message_mqtt('Weight')
on_message_maturity = on_message_mqtt('Maturity')
on_message_ripeness = on_message_mqtt('Flurescence spectrometer')

on_message_soil = on_message_mqtt('Soil Moisture')
on_message_uv = on_message_mqtt('UV Sensor')
on_message_wind = on_message_mqtt('Wind Speed')

on_message_noise = on_message_mqtt('Ambient Noise')
on_message_turnover = on_message_mqtt('Table Turnover')
on_message_wait = on_message_mqtt('Wait Time')

on_message_smell = on_message_mqtt('Smell Intensity')
on_message_co2 = on_message_mqtt('CO2 Concentration')
on_message_dish = on_message_mqtt('Dishwashing Frequency')


client = mqtt.Client()

client.message_callback_add('hewantelur/yolkcolor', on_message_yolkcolor)
client.message_callback_add('hewantelur/ammonia', on_message_ammonia)
client.message_callback_add('hewantelur/bacterial', on_message_bacterial)

client.message_callback_add('redmeat/humidity', on_message_humidity)
client.message_callback_add('redmeat/ozone', on_message_ozone)
client.message_callback_add('redmeat/gas', on_message_gas)

client.message_callback_add('whitemeat/fat', on_message_fat)
client.message_callback_add('whitemeat/impedance', on_message_impedance)
client.message_callback_add('whitemeat/ph', on_message_ph)

client.message_callback_add('grains/moisture', on_message_moisture)
client.message_callback_add('grains/texture', on_message_texture)
client.message_callback_add('grains/density', on_message_density)

client.message_callback_add('veg/activity', on_message_activity)
client.message_callback_add('veg/ethylene', on_message_ethylene)
client.message_callback_add('veg/temperature', on_message_temperature)

client.message_callback_add('fruits/weight', on_message_weight)
client.message_callback_add('fruits/maturity', on_message_maturity)
client.message_callback_add('fruits/ripeness', on_message_ripeness)

client.message_callback_add('weather/soil', on_message_soil)
client.message_callback_add('weather/uv', on_message_uv)
client.message_callback_add('weather/wind', on_message_wind)

client.message_callback_add('sales/noise', on_message_noise)
client.message_callback_add('sales/turnover', on_message_turnover)
client.message_callback_add('sales/waittime', on_message_wait)

client.message_callback_add('customer/smell', on_message_smell)
client.message_callback_add('customer/co2', on_message_co2)
client.message_callback_add('customer/dishwashing', on_message_dish)

client.on_connect = on_connect

client.connect(settings.MQTT_HOST, settings.MQTT_PORT)
