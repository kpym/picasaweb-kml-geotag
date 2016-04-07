# picasaweb-kml-geotag

This is a small script to geotag pictures from Picasaweb `.kml`.

## Description of the problem

When we geotag files in picasaweb, the information is not saved inside the file's exif.
If you want to use this pisasa geotag information to geotag the local copies of your pictures there are several possibilities :
- one is to use the picasaweb API to recover the information
- another one is to use the `.kml` file available in every Picasaweb folder.

This script use the second method.

## How it works

When you download a `.kml` file from Picasaweb folder it contains some data that can be extracted to geotag your local pictures.
These files contain sequence of informations like this one:

    <Placemark id='entryXXX'>
      ....
      src="https://lh3.googleusercontent.com/.../picture.jpg"
      ....
      <Point>
        <coordinates>10.4851755,43.8500234</coordinates>
      </Point>
    </Placemark>

This python script run over all `.kml` files in the folder. And for every picture, if it exists in the folder, the script runs `exiftools` to writhe the geodata.

## How to use it

- Download `.kml` file from picasaweb and save it in a folder containing the original pictures.
- Backup your pictures (this script overwrite them, so in case of a problem when writing ...) !
- Run the script, for example like this

        python -u pwgeotag.py


