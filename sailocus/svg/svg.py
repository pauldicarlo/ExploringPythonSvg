'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''

import svgwrite

from sailocus.geometry.triangle import Triangle
from sailocus.geometry.point import Point
from sailocus.geometry.line import intersection, Line

from sailocus.sail.sail import Sail
from sailocus.sail.sail import TriangleCenterOfEffort

class SVG():

    def __init__(sel ):
        pass

    def writeToFile(self, sail, pathToFile, off_set=0):
        points = sail.getAsPoints()

        #TODO - need to handle offest for entire set of points/polygons/etc
        off_set = (0,0)

        canvas_size, points = recalculate(points, off_set)
        width, height = canvas_size

        dwg = svgwrite.Drawing(pathToFile, size=(str(canvas_size[0])+'px', str(canvas_size[1])+'px'))
        transform_group = dwg.g(transform=f"translate(0, {height}) scale(1, -1)")

        #dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='darkkhaki'))
        dwg.add(dwg.rect(insert=(0, 0), size=(str(canvas_size[0])+'px', str(canvas_size[1])+'px'), fill='darkseagreen'))

        # dwg.add(dwg.line((10, 50), (250, 100), stroke='blue', stroke_width=5))


        trapezoid = dwg.polygon(
            points=points,
            fill='ivory',
            stroke='black',
            stroke_width=1
        )
        transform_group.add(trapezoid)

        # draw line from throat to clew
        transform_group.add(dwg.line(sail.throat, sail.clew, stroke='black', stroke_width=1, stroke_dasharray='9,5'))

        # this will only work for a 4 sided sail...

        # NOTE: Methodology here:  https://drive.google.com/file/d/1bCS8gZQXRBTjdJaQH7uB7qPAZpiGT_Ts/view?usp=sharing 
        # Sail.coe has all of the following lines and coe calculated.  
        # Here we just put them into the SVG
        # line from one triangle of the sail centroid to the other
        transform_group.add(dwg.line(sail.coe.triangles[0].centroid, sail.coe.triangles[1].centroid, stroke='red', stroke_width=1))
        # then get the lines perpendicular to that line between centroids...
        for line_segment in sail.coe.lines_perpendicular_to_centroid_line_segments:
            transform_group.add(dwg.line(line_segment.point_a , line_segment.point_b, stroke='purple', stroke_width=2))
        # and the line from end point of vectors from perpendicuar lines
        transform_group.add(dwg.line(
            sail.coe.lines_perpendicular_to_centroid_line_segments[0].point_b,
            sail.coe.lines_perpendicular_to_centroid_line_segments[1].point_b,
            stroke='blue', stroke_width=1))
        # at this point, we have an intersection of the following:
        #      1. line from one triangle of the sail centroid to the other 
        #     2. ine from end point of vectors from perpendicuar lines
        # the intersection of which gives us sail.coe.center_of_effort which has already been calculated

        # Need an inner group that flips again so text will be in right orientation 
        text_group = transform_group.add(dwg.g(transform="scale(1, -1)"))  # Flip back!

        # TODO: Make this better.
        text_group.add(dwg.text('tack', insert=(sail.tack.x+5, -1 *(sail.tack.y) - 250), fill='black', font_size='20px'))
        text_group.add(dwg.text('throat', insert=(10,-40), fill='black', font_size='20px'))
        text_group.add(dwg.text('clew', insert=(sail.clew.x-40, -sail.clew.y), fill='black', font_size='20px'))
        text_group.add(dwg.text('peak', insert=(sail.peak.x, -(sail.peak.y) +50 ), fill='black', font_size='20px'))

        transform_group.add(dwg.circle(center=(sail.coe.center_of_effort), r=2, fill='blue', stroke='black', stroke_width=1))
        text_group.add(dwg.text('COE', insert=(sail.coe.center_of_effort.x, -sail.coe.center_of_effort.x), fill='black', font_size='20px'))



        dwg.add(transform_group)
        dwg.save()
        
def recalculate(points, off_set):

    maxX = 0
    maxY = 0

    updated_points = []

    # TODO ensure that points are in sequence and make sense 

    off_set_x, off_set_y = off_set

    for x,y in points:
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y        
        updated_points.append((x+off_set_x, y+off_set_y))

    print("maxX=", maxX, " maxY=", maxY)

    canvas_size = (maxX + 2*off_set_x, maxY + 2*off_set_y)

    return canvas_size, updated_points
