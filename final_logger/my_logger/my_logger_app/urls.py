from django.contrib import admin
from django.urls import path , include
from my_logger_app import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(my_logger_app.urls))
]
