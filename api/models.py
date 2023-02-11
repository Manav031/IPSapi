from django.db import models

# Create your models here.
class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    building_name = models.CharField(max_length=500, null=True, blank=True)
    floor = models.IntegerField(null=True, blank=True)

class AccessPoint(models.Model):
    ap_id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(Building, on_delete=models.CASCADE)
    bssid = models.CharField(max_length=500, null=True, blank=True)
    mac_address = models.CharField(max_length=500, null=True, blank=True)

class Location(models.Model):
    loc_id = models.AutoField(primary_key=True)
    ap_id = models.ForeignKey(AccessPoint, on_delete=models.CASCADE)
    room_name = models.CharField(max_length=255, null=True, blank=True)
    range_start = models.IntegerField(null=True, blank=True)
    range_end = models.IntegerField(null=True, blank=True)
    far_from_ap_m = models.FloatField(null=True, blank=True)

"""
    req structure
    it will first make request with mac address and find the ap in db if not find than ask for building name and register it using post
    than while clicking on callibrate button it should initialize get rssi function and there should be random number calls between 40 to 60 and 
    between eaxch rssi value it should wait for 1 second than collecting all data it should go and push the data to end point
"""