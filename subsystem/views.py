from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

import joblib
from machinelearning import mlmodel

from .models import Sensor, SensorLog, Actuator, ActuatorLog

class SensorTemplateView(APIView):
    sensor_name = ""
    def get(self, request, format=None):
        sensor = Sensor.objects.get(name=self.sensor_name)
        data = {
            "value": sensor.value
        }
        return Response(data)

class ActuatorTemplateView(APIView):
    actuator_name = ""
    sensor1_name = ""
    sensor2_name = ""
    sensor3_name = ""
    training_csv = ""
    def get(self, request, format=None):
        actuator = Actuator.objects.get(name=self.actuator_name)
        sensor1 = Sensor.objects.get(name=self.sensor1_name)
        sensor2 = Sensor.objects.get(name=self.sensor2_name)
        sensor3 = Sensor.objects.get(name=self.sensor3_name)
        model = mlmodel.BaseLinearRegression(settings.ML_ROOT + self.training_csv)
        prediction = model.predict([float(sensor1.value), float(sensor2.value), float(sensor3.value)])
        actuator.state = int(prediction)
        actuator.save()
        data = {
            "state": actuator.state
        }
        return Response(data)

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')

# Water Heating System
class WaterTemperatureView(SensorTemplateView):
    sensor_name = "Water Temperature"
    
class WaterUsageRateView(SensorTemplateView):
    sensor_name = "Water Usage Rate"

class OutsideTemperatureView(SensorTemplateView):
    sensor_name = "Outside Temperature"
    
class WaterHeaterView(ActuatorTemplateView):
    actuator_name = "Water Heater"
    sensor1_name = "Water Temperature"
    sensor2_name = "Water Usage Rate"
    sensor3_name = "Outside Temperature"
    training_csv = "heater.csv"

# Fan Control System
class RoomTemperatureView(SensorTemplateView):
    sensor_name = "Room Temperature"
    
class RoomHumidityView(SensorTemplateView):
    sensor_name = "Room Humidity"
    
class RoomCO2View(SensorTemplateView):
    sensor_name = "Room CO2"
    
class VentilationFanView(ActuatorTemplateView):
    actuator_name = "Ventilation Fan"
    sensor1_name = "Room Temperature"
    sensor2_name = "Room Humidity"
    sensor3_name = "Room CO2"
    training_csv = "fan.csv"
    
# Lighting Control System
class LightLevelView(SensorTemplateView):
    sensor_name = "Light Level"
    
class OccupancyView(SensorTemplateView):
    sensor_name = "Occupancy"
    
class DaylightView(SensorTemplateView):
    sensor_name = "Daylight"

class LightingSystemView(ActuatorTemplateView):
    actuator_name = "Lighting System"
    sensor1_name = "Light Level"
    sensor2_name = "Occupancy"
    sensor3_name = "Daylight"
    training_csv = "light.csv"