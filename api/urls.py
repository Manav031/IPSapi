from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_end_points, name="all_end_points"),
    path('building/', views.BuildingList.as_view(), name="building_list"),
    path('buildings/<pk>/', views.BuildingDetail.as_view(), name="building_detail"),
    path('accesspoints/', views.AccessPointList.as_view(), name="accesspoint_list"),
    path('accesspoints/<pk>/', views.AccessPointDetail.as_view(), name="accesspoint_detail"),
    path('locations/', views.LocationList.as_view(), name="location_list"),
    path('locations/<pk>/', views.LocationDetail.as_view(), name="location_detail"),
    path('check_mac/', views.check_mac, name='check_mac')
]