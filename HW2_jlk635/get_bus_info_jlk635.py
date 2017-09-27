from __future__ import print_function
import sys
import pylab as pl
import os
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_jlk635.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()

MTAKEY =  str(sys.argv[1])
BusRef =  str(sys.argv[2])
    
url= "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + MTAKEY + "&VehicleMonitoringDetailLevel=calls&LineRef=" + BusRef

response = urllib.urlopen(url)
read_data = response.read()
#print(read_data)
data = json.loads(read_data)

AllBuses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# this line opens a file for writing using the name you chose
# the "w" tells it you are opening for writing, not reading
fout = open(sys.argv[3], "w")     #open(sys.argv[1], "w")

fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

# this line prints Latitude,Longitude,Stop Name,Stop Status 
#for each of the buses from nominated route
# notice the "\n" character at the end of each line:
# that's the line break
BusCounter = 0
for it in AllBuses:
    Lon = str(it['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    Lat = str(it['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    key = (it['MonitoredVehicleJourney']['OnwardCalls'] == {})
  
    if key:
        StopName = 'N/A'
        StopStatus = 'N/A'
    else:
        StopName = str(it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'])
        StopStatus = str(it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']) #The next stop for Bus 0 of active buses      
    fout.write(str('{},{},{},{}\n'.format(Lat, Lon, StopName, StopStatus)))
    BusCounter += 1

