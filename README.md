# lotss-cutout-api
Example Python scripts for the LoTSS cutout server API

## purpose

This script provides an example of a Python user interface to the LoTSS cutout server API.

## prerequisites

The script relies on the Python `requests` package. You must install `requests` before the code can be used.

## usage

Look at and if necessary modify `cutout.py`. The `get_cutout()`
function will grab files from the web server. As with the web-based
interface, the `pos` keyword can be an object name, in which case it
will be resolved by the remote server, or co-ordinates such as
`12:34:56.7 +45:60:01.2`. Making this function handle other input
position types such as an astropy Skycoord or an ra,dec pair in
degrees is left as an exercise for the reader.

The example main
function in `cutout.py` will download images of a list of objects from
the server, storing them in FITS files in the working directory. If
you run it on the provided input file `test.txt` it should download
some images to demonstrate that the code is working.
