
    
from __future__ import print_function
import sys
import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# this line checks how many arguments are passed to python
# the arguments are stored in sys.argv which is a list
# the first argument is the name of the code
# so sys.argv is a list with at least one element
# with your name in input it will be a list of 2
# if you add more than one word as argument it will give you an error as well
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python  show_bus_locations_jlk635.py <MTA_KEY> <BUS_LINE>")
    sys.exit()


MTAKEY =  str(sys.argv[1])
BusRef =  str(sys.argv[2])
    

url= "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTAKEY + "&VehicleMonitoringDetailLevel=calls&LineRef=" + BusRef
    
    
response = urllib.urlopen(url)
data = response.read()
data = json.loads(data)


AllBuses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'] #this is vehicle activity for the buses on the given route


Buses = len(AllBuses)
type(BusRef)
print ('Bus Line : {}'.format(BusRef)) 
print ('Number of Active Buses : {}'.format(Buses)) 
BusCounter = 0
for it in AllBuses:
    Lon = str(it['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    Lat = str(it['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    print ('Bus {} is at latitude {} and longitude {}'.format(BusCounter,Lat, Lon))
    BusCounter += 1



