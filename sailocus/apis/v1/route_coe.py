'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''


from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field

from sailocus.sail import sail
from sailocus.geometry import point
from sailocus.svg import svg

router = APIRouter()

class FourSidedSailParameters(BaseModel):
    tack_x: int = Field(..., ge=0, le=2000, description="X position in mm of Tack")
    tack_y: int = Field(..., ge=0, le=2000, description="Y position in mm of Tack")

    throat_x: int = Field(..., ge=0, le=2000, description="X position in mm of Throat")
    throat_y: int = Field(..., ge=0, le=2000, description="Y position in mm of Throat")

    peak_x: int = Field(..., ge=0, le=2000, description="X position in mm of Peak")
    peak_y: int = Field(..., ge=0, le=2000, description="Y position in mm of Peak")

    clew_x: int = Field(..., ge=0, le=2000, description="X position in mm of Clew")
    clew_y: int = Field(..., ge=0, le=2000, description="Y position in mm of Clew")




@router.get("/")
def get_coe(parameters: FourSidedSailParameters):
#def get_coe():
    """Generate an SVG that visualizes the specified (x, y) coordinate."""
    try:

        # Create the sail and render it to a SVG representation 
        xsail = sail.Sail(tack=point.Point(parameters.tack_x, parameters.tack_y),
            throat=point.Point(parameters.throat_x, parameters.throat_y),
            peak=point.Point(parameters.peak_x, parameters.peak_y),
            clew=point.Point(parameters.clew_x, parameters.clew_y))
        xsail.validateSail()
        xsvg = svg.SVG()
        pathToFile = "./simpleSailFromClass.svg"
        off_set = point.Point(25,25)
        svg_content =  xsvg.createSailSVG(xsail, pathToFile, True, off_set)

        # svg_content = create_coordinate_svg(parameters.x, parameters.y)
        return Response(
            content=svg_content.tostring(),
            media_type="image/svg+xml",
            headers={"Content-Disposition": f"inline; filename=coordinate_{parameters.peak_x}_{parameters.peak_y}.svg"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating SVG: {str(e)}")

    return {"message": "Hello, At this point something should happen, but at least you know you got here"}