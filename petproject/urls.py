from django.contrib import admin
from django.urls import path
from petapp import views
from petapp.views.serviceView import ServiceCreateView, ServiceUpdateView, ServiceListView, ServiceDetailView, ServiceDelateView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path('service/create/', views.ServiceCreateView.as_view()),
    path('service/<int:pk>/', views.ServiceDetailView.as_view()),
    path('service/update/<int:pk>/', views.ServiceUpdateView.as_view()),
    path('service/remove/<int:pk>/', views.ServiceDelateView.as_view()),
    path('services/', views.ServiceListView.as_view())
]




