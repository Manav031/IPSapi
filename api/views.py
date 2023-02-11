from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Building, AccessPoint, Location
from .serializers import BuildingSerializer, AccessPointSerialzer, LocationSerializer
# Create your views here.

@api_view(['GET'])
def all_end_points(request):
    resp = {
        "all": "/api/",
        "buildings": "/api/buildings/",
        "accessPoints": "/api/accesspoints/",
        "locations": "/api/locations"
    }

    return Response(resp, status.HTTP_200_OK)

class BuildingList(APIView):
    serializer_class = BuildingSerializer

    def get(self, request):
        all_building_data = Building.objects.all()
        building_data_serializer = self.serializer_class(all_building_data, many=True)
        context = {"parameters": "{'building_name', 'floor'}", "data": building_data_serializer.data}
        return Response(context, status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            err_msg = {
                "detail": "An Error occured",
                "data": serializer.data,
                "error": serializer.errors
            }
            return Response(err_msg, status.HTTP_400_BAD_REQUEST)

class BuildingDetail(APIView):
    serializer_class = BuildingSerializer

    def get_object(self, pk):
        try:
            return Building.objects.get(building_id=pk)
        except Building.DoesNotExist:
            return None

    def get(self, request, pk):
        building = self.get_object(pk)
        if building:
            serializer = self.serializer_class(building)
            return Response(serializer.data)
        else:
            return Response({"detail": "No data found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        building = self.get_object(pk)
        if building:
            serializer = self.serializer_class(building, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "No data found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        buildng = self.get_object(pk)
        if buildng:
            buildng.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "No data found"}, status=status.HTTP_404_NOT_FOUND)

class AccessPointList(APIView):
    serializer_class = AccessPointSerialzer

    def get(self, request):
        all_accesspoint_data = AccessPoint.objects.all()
        accesspoint_data_serializer = self.serializer_class(all_accesspoint_data, many=True)
        context = {"parameters": "{'building_id', 'bssid', 'mac_address', 'range_start', 'range_end'}", "data": accesspoint_data_serializer.data}
        return Response(context, status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            err_msg = {
                "detail": "An Error occured",
                "data": serializer.data,
                "error": serializer.errors
            }
            return Response(err_msg, status.HTTP_400_BAD_REQUEST)

class AccessPointDetail(APIView):
    serializer_class = AccessPointSerialzer

    def get_object(self, pk):
        try:
            return AccessPoint.objects.get(ap_id=pk)
        except Building.DoesNotExist:
            return None

    def get(self, request, pk):
        access_point = self.get_object(pk)
        if access_point:
            serializer = self.serializer_class(access_point)
            return Response(serializer.data)
        else:
            return Response({"detail": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        access_point = self.get_object(pk)
        if access_point:
            serializer = self.serializer_class(access_point, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        buildng = self.get_object(pk)
        if buildng:
            buildng.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)


class LocationList(APIView):
    serializer_class = LocationSerializer

    def get(self, request):
        all_location_point = Location.objects.all()
        all_location_serializer = self.serializer_class(all_location_point, many=True)
        context = {"parameters": "{'ap_id', 'room_name', 'rssi_value'}", "data": all_location_serializer.data}
        return Response(context, status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            err_msg = {
                "detail": "An error occured",
                "data": serializer.data,
                "error": serializer.errors
            }
            return Response(err_msg, status=status.HTTP_400_BAD_REQUEST)

class LocationDetail(APIView):
    serializer_class = LocationSerializer

    def get_object(self, pk):
        try:
            return Location.objects.get(loc_id=pk)
        except Location.DoesNotExist:
            return None

    def get(self, request, pk):
        location = self.get_object(pk)
        if location:
            serializer = self.serializer_class(location)
            return Response(serializer.data)
        else:
            return Response({"detail": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        location = self.get_object(pk)
        if location:
            serializer = self.serializer_class(location, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        location = self.get_object(pk)
        if location:
            location.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "No Data Found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def check_mac(request):
    mac_address = request.GET['mac_address']
    rssi_value = request.GET['rssi']
    ap_details = AccessPoint.objects.filter(mac_address=mac_address)
    if ap_details.exists():
        location_data = dict()
        locations = Location.objects.filter(ap_id=ap_details[0].ap_id)
        building_data = Building.objects.filter(building_id=ap_details[0].building_id.building_id)[0]
        for location in locations:
            if int(rssi_value) in range(location.range_start, location.range_end):
                location_data['location_name'] = location.room_name
                location_data['far_from_ap'] = location.far_from_ap_m
        return Response({"detail": True, "location_data": location_data, 'building_name': building_data.building_name + "-" + str(building_data.floor)}, status=status.HTTP_200_OK)
    return Response({"detail": False}, status=status.HTTP_404_NOT_FOUND)