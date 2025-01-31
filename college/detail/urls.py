from django.urls import path,include
from detail.routers import router

url=[
    path("college/",include(router.urls)),
]   
# from django.urls import path
# from . import views  # Import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
# ]
