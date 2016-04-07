#!/usr/bin/env python

import re
import os
import sys
from subprocess import call

# the name of the exiftool executable
# you can replace it with a full path to the executable
exiftool = "exiftool"

# check if exiftool is accessible
try:
  print "Check exiftool version ..."
  call([exiftool,"-ver"])
  print "...ok\n\n"
except:
  print "Can't find exiftool. Make sure that it is in the PATH."
  sys.exit()

# intro message and ask if to continue
print """
This script will search for picasaweb kml files.
If any, it will loop over all geotag info inside.
For any picture, if the local file with the same name exists,
it will use exiftool (which must be in the current path)
to write the gps coordinates inside the exif part.\n
*** Backup your pictures before (in case of a problem) !!! ***\n
"""
sys.stdout.flush()

if not raw_input("Do you want to continue ? [Y]es or [N]o :").lower().startswith("y") :
  sys.exit()


# patern to find filename, longitude and latitude
p = re.compile(ur'(?<=\d/)([^/]+?\.jpg).*?(?<=<coordinates>)([\d.]+),([\d.]+)', re.IGNORECASE)

# loop over all kml files
for file in os.listdir("."):
    if file.endswith(".kml"):
      print "\n=================\n" + file + "\n=================\n"
      sys.stdout.flush()
      with open(file, 'r') as kmlfile:
          data=kmlfile.read()
      # loop over all pictures from the kml file
      for m in re.finditer(p, data):
        if os.path.isfile(m.group(1)) :
          print "%(file)s => (%(lng)s,%(lat)s) ..." % {'file': m.group(1), "lng": m.group(2), "lat": m.group(3) }
          sys.stdout.flush()
          call([exiftool,"-GPSLongitude="+m.group(2), "-GPSLatitude="+m.group(3), m.group(1)])

