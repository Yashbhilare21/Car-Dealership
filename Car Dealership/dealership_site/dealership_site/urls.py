from django.contrib import admin
from django.urls import path, include
from cars.views import car_list  # Import the view directly
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls')),
    path('', car_list),  # 👈 Set the root URL to show the car list
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)