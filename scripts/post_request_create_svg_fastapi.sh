#!/bin/bash

export PEAK_X=213
export PEAK_X=510
export THROAT_X=10
export THROAT_Y=233
export TACK_X=0
export TACK_Y=0
export CLEW_X=397 
export CLEW_Y=29 




export API_PATH=sailocus/api/v1/coe/ 


curl -v -X GET  "http://localhost:8000/${API_PATH}" \
  -H "Content-Type: application/json" \
  -d '{ "peak_x": 213, "peak_y": 510, "clew_x": 397,  "clew_y": 29, "tack_x": 0,   "tack_y": 0, "throat_x": 10, "throat_y": 233 }' \
  --output coordinate_point.svg
