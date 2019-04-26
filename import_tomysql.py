#!/usr/bin/env python3

import os
import json
from jinja2 import Template

with open("/Users/jorge/code/lab/autobackup/data1.json", "r") as json_file:
    data = json.load(json_file)

#print("data:", data)
for item in data:
#after longitude there are 4 values to understand | gpsAge | speedKPH | heading | altitude |
#differences between time and lastgps_time
    template_line = "INSERT INTO `EventData` VALUES ('{{account}}','{{device}}',{{time.epoch_time}},{{deviceData.gpsdata.event}},{{deviceData.gpsdata.latitude}},{{deviceData.gpsdata.longitude}},10,{{deviceData.gpsdata.speed}},{{deviceData.gpsdata.heading}},{{deviceData.gpsdata.altitude}},'',0,0,0,'{{deviceData.gpsdata.address}}','','',{{deviceData.gpsdata.distancedelta}},{{deviceData.mileage}},0,0,'',{{time.epoch_time}},'','','','','','',0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,'',0,'',0,'',0,0,0,'','','','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,'','',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'',0,0,0,'','','','','','')"
    #template_line = "$vehicle ... $account ... $time.epoch_time"
    tm = Template(template_line)
    line = tm.render(item)
    print(line)
