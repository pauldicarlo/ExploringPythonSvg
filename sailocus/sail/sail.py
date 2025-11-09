'''
@author: Paul DiCarlo
@copyright: 2025 Paul DiCarlo
@license: MIT
@contact: https://github.com/pauldicarlo
'''
class Sail(object):

    ################################################################
    def __init__(self, tack, clew, head=None, peak=None, throat=None, sailName = None):
    
        self.sailName = sailName 
        
        params = "tack="+str(tack)+", clew="+str(clew)+", head="+str(head)+", peak="+str(peak)+", throat="+str(throat)
        
        bHead = head is not None
        bPeak = peak is not None
        bThroat = throat is not None
        
        print(params)
        if (bHead and bPeak and bThroat) or (not bHead and not bPeak and not bThroat) :
            raise ValueError('Sail constructor: head, peak, and throat cannot all populated or non empty.  params=' + params)
        if (bPeak and not bThroat) or (not bPeak and bThroat):
            raise ValueError('Sail constructor: If peak or throat is populated, then both must be. params=' + params)
        
        self.peak = peak
        self.throat = throat
        self.tack = tack
        self.clew = clew
        self.head = head
        
        
        self.POINT_NAME_PEAK = "Peak"
        self.POINT_NAME_THROAT = "Throat"
        self.POINT_NAME_TACK = "Tack"
        self.POINT_NAME_CLEW = "Clew"
        self.POINT_NAME_HEAD = "Head"
        
        self.calculateCenterOfEffort()

    ################################################################
    def __str__(self):
        return "[peak=" + str(self.peak) + ",throat=" + str(self.throat) + \
            ", tack=" + str(self.tack) + ", clew=" + str(self.clew) + ", head=" + str(self.head) +"]"

    ################################################################
    # peak throat
    # tack clew
    def validateSail(self):
        if self.peak.y <= self.tack.y or self.peak.y <= self.clew.y:
            raise ValueError("Peak must have y value greater than tack or clew. \n" +str(self) )
        return


    ################################################################
    # Returns the number of sides.  3 it's a triangle.
    # 4 it's a sprit or lug or something like that
    def getNumSides(self):
        if self.head is None:
            return 4
        return 3

    ################################################################
    def calculateCenterOfEffort(self):
        # TODO implement
        pass