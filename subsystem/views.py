from django.shortcuts import render
from django.views.generic import View
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

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
    model = ""
    def get(self, request, format=None):
        actuator = Actuator.objects.get(name=self.actuator_name)
        sensor1 = Sensor.objects.get(name=self.sensor1_name)
        sensor2 = Sensor.objects.get(name=self.sensor2_name)
        sensor3 = Sensor.objects.get(name=self.sensor3_name)
        prediction = self.model.predict([float(sensor1.value), float(sensor2.value), float(sensor3.value)])
        actuator.state = int(prediction)
        actuator.save()
        data = {
            "state": actuator.state
        }
        return Response(data)

class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home.html')


# Susu Hewani dan Telur
class YolkColorView(SensorTemplateView):
    sensor_name = "Yolk Color Hue"
    
class AmmoniaView(SensorTemplateView):
    sensor_name = "Ammonia"

class DairyBacterialView(SensorTemplateView):
    sensor_name = "Dairy Bacterial"
    
class AirPurifierView(ActuatorTemplateView):
    actuator_name = "Air Purifier"
    sensor1_name = "Yolk Color Hue"
    sensor2_name = "Ammonia"
    sensor3_name = "Dairy Bacterial"
    model = mlmodel.air_purifier_model


# Daging Merah
class HumidityView(SensorTemplateView):
    sensor_name = "Humidity"
    
class OzoneView(SensorTemplateView):
    sensor_name = "Ozone"

class GasView(SensorTemplateView):
    sensor_name = "Gas"

class WaterMistingView(ActuatorTemplateView):
    actuator_name = "Water Misting"
    sensor1_name = "Humidity"
    sensor2_name = "Ozone"
    sensor3_name = "Gas"
    model = mlmodel.red_meat_model
    
    
# Daging Putih
class NIRView(SensorTemplateView):
    sensor_name = "NIR Spectroscopy"
    
class ImpedanceView(SensorTemplateView):
    sensor_name = "Impedance"

class pHView(SensorTemplateView):
    sensor_name = "pH"
    
class VinegarSprayerView(ActuatorTemplateView):
    actuator_name = "Vinegar Sprayer"
    sensor1_name = "NIR Spectroscopy"
    sensor2_name = "Impedance"
    sensor3_name = "pH"
    model = mlmodel.white_meat_model
 
    
# Beras, Gandum, Jagung
class HyperspectralView(SensorTemplateView):
    sensor_name = "Hyperspectral Imaging"
    
class AcousticView(SensorTemplateView):
    sensor_name = "Acoustic"

class CapacitiveView(SensorTemplateView):
    sensor_name = "Capacitive"

class InfraredHeaterView(ActuatorTemplateView):
    actuator_name = "Infrared Heater"
    sensor1_name = "Hyperspectral Imaging"
    sensor2_name = "Acoustic"
    sensor3_name = "Capacitive"
    model = mlmodel.grain_model
    
 
# Sayuran
class ChlorophyllView(SensorTemplateView):
    sensor_name = "Chlorophyll Fluorescence"
    
class EthyleneView(SensorTemplateView):
    sensor_name = "Ethylene"

class TemperatureView(SensorTemplateView):
    sensor_name = "Temperature"

class LEDGrowLightView(ActuatorTemplateView):
    actuator_name = "LED Grow Light"
    sensor1_name = "Chlorophyll Fluorescence"
    sensor2_name = "Ethylene"
    sensor3_name = "Temperature"
    model = mlmodel.veg_model


# Buah-buahan
class WeightView(SensorTemplateView):
    sensor_name = "Weight"
    
class MaturityView(SensorTemplateView):
    sensor_name = "Maturity"

class SpectrometerView(SensorTemplateView):
    sensor_name = "Flurescence spectrometer"
    
class HumidifierView(ActuatorTemplateView):
    actuator_name = "Humidifier"
    sensor1_name = "Weight"
    sensor2_name = "Maturity"
    sensor3_name = "Flurescence spectrometer"
    model = mlmodel.fruit_model
    
    
# Deteksi Musim
class SoilView(SensorTemplateView):
    sensor_name = "Soil Moisture"
    
class UVView(SensorTemplateView):
    sensor_name = "UV Sensor"

class WindView(SensorTemplateView):
    sensor_name = "Wind Speed"

class HVACView(ActuatorTemplateView):
    actuator_name = "HVAC"
    sensor1_name = "Soil Moisture"
    sensor2_name = "UV Sensor"
    sensor3_name = "Wind Speed"
    model = mlmodel.weather_model
    
    
# Deteksi Hasil Penjualan Berfluktuasi
class NoiseView(SensorTemplateView):
    sensor_name = "Ambient Noise"
    
class TurnoverView(SensorTemplateView):
    sensor_name = "Table Turnover"

class WaitView(SensorTemplateView):
    sensor_name = "Wait Time"

class SalesView(ActuatorTemplateView):
    actuator_name = "Estimated Sales"
    sensor1_name = "Ambient Noise"
    sensor2_name = "Table Turnover"
    sensor3_name = "Wait Time"
    model = mlmodel.sales_model

    
# Deteksi Jumlah Pengunjung Restoran
class SmellView(SensorTemplateView):
    sensor_name = "Smell Intensity"
    
class CO2View(SensorTemplateView):
    sensor_name = "CO2 Concentration"

class DishView(SensorTemplateView):
    sensor_name = "Dishwashing Frequency"
    
class CustomerView(ActuatorTemplateView):
    actuator_name = "Number Of Customers"
    sensor1_name = "Smell Intensity"
    sensor2_name = "CO2 Concentration"
    sensor3_name = "Dishwashing Frequency"
    model = mlmodel.customer_model