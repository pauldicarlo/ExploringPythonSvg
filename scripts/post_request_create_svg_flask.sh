#!/bin/bash
# @author: Paul DiCarlo
# @copyright: 2025 Paul DiCarlo
# @license: MIT
# @contact: https://github.com/pauldicarlo

export PEAK="(213,510)"
export THROAT="(10,233)"
export TACK="(0,0)" 
export CLEW="(397,29)" 



/usr/bin/curl -o ./somefile.svg -v -X POST \
    "http://127.0.0.1:5000/generate-svg?peak=$PEAK&throat=$THROAT&tack=$TACK&clew=$CLEW"
