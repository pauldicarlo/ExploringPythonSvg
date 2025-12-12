from sailocus.sail import sail
from sailocus.geometry import point
from sailocus.svg import svg

# we're making a 4-sided sail here so we need
# to have the peak, throat, take, and clew...
# Point(x,y) where x/y are millimeters and ints
peak = point.Point(213, 510)
throat = point.Point(10, 233)
tack = point.Point(0, 0) 
clew = point.Point(397, 29) 

# create a Sail with the points
xsail = sail.Sail(tack=tack, clew=clew, head=None, peak=peak, throat=throat, sail_name = "Four sided sail")
xsail.validateSail()
print(f"CoE={xsail.coe}")

# Create SVG file of sail and its CoE
xsvg = svg.SVG()
pathToFile = "./simpleSailFromClass.svg"
off_set = point.Point(25,25)
xsvg.createSailSVG(xsail, pathToFile, True, off_set)