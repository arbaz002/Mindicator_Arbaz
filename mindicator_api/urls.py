from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url
from rest_framework import routers

from app import views


router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'station', views.StationViewSet)
router.register(r'train', views.TrainViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include(router.urls)),
    path('app/sites/list/<str:arrival_station_name>/<str:sort_by_arrival_time>',views.TrainList.as_view(),name="trainlist"),
    path('app/user/login',views.verifyUser,name="verifyUser"),
]
