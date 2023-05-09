from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view()),
    
    # Susu Hewani dan Telur
    path('sensor/yolk', views.YolkColorView.as_view()),
    path('sensor/ammonia', views.AmmoniaView.as_view()),
    path('sensor/bacteria', views.DairyBacterialView.as_view()),
    path('actuator/purifier', views.AirPurifierView.as_view()),
    
    # Daging Merah
    path('sensor/humidity', views.HumidityView.as_view()),
    path('sensor/ozone', views.OzoneView.as_view()),
    path('sensor/gas', views.GasView.as_view()),
    path('actuator/misting', views.WaterMistingView.as_view()),
    
    # Daging Putih
    path('sensor/fat', views.NIRView.as_view()),
    path('sensor/impedance', views.ImpedanceView.as_view()),
    path('sensor/ph', views.pHView.as_view()),
    path('actuator/vinegar', views.VinegarSprayerView.as_view()),
    
    # Beras, Gandum, Jagung
    path('sensor/moisture', views.HyperspectralView.as_view()),
    path('sensor/texture', views.AcousticView.as_view()),
    path('sensor/density', views.CapacitiveView.as_view()),
    path('actuator/heater', views.InfraredHeaterView.as_view()),
    
    # Sayuran
    path('sensor/activity', views.ChlorophyllView.as_view()),
    path('sensor/ethylene', views.EthyleneView.as_view()),
    path('sensor/temperature', views.TemperatureView.as_view()),
    path('actuator/growlight', views.LEDGrowLightView.as_view()),
    
    # Buah-buahan
    path('sensor/weight', views.WeightView.as_view()),
    path('sensor/maturity', views.MaturityView.as_view()),
    path('sensor/ripeness', views.SpectrometerView.as_view()),
    path('actuator/humidifier', views.HumidifierView.as_view()),
    
    # Deteksi Musim
    path('sensor/soil', views.SoilView.as_view()),
    path('sensor/uv', views.UVView.as_view()),
    path('sensor/wind', views.WindView.as_view()),
    path('actuator/hvac', views.HVACView.as_view()),
    
    # Deteksi Hasil Penjualan Berfluktuasi
    path('sensor/noise', views.NoiseView.as_view()),
    path('sensor/turnover', views.TurnoverView.as_view()),
    path('sensor/wait', views.WaitView.as_view()),
    path('actuator/sales', views.SalesView.as_view()),
    
    # Deteksi Jumlah Pengunjung Restoran
    path('sensor/smell', views.SmellView.as_view()),
    path('sensor/co2', views.CO2View.as_view()),
    path('sensor/dish', views.DishView.as_view()),
    path('actuator/customer', views.CustomerView.as_view()),
    
    path('actuator/power', views.PowerView.as_view()),
    path('actuator/harvest', views.HarvestView.as_view()),
    path('actuator/stock', views.StockView.as_view()),
    path('actuator/performance', views.PerformanceView.as_view()),
]