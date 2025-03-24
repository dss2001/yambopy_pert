# Copyright (c) 2018, Henrique Miranda
# All rights reserved.
#
# This file is part of the yambopy project
#
from yambopy import *
from yambopy.plot import *
import os

ha2ev = 27.211396132

class YamboRT_Carriers_DB(object):
    """
    Open the RT databases and store it in a RTDB class.
    So far treating COHERENT runs: reading polarization and carriers.
    """

    def __init__(self,folder='.',calc='.',carriersdb='ndb.RT_carriers'):
        # Find path with RT data
        carrpath = '%s/%s/%s'%(folder,calc,carriersdb)

        try:
            data_carr= Dataset(carrpath)
        except:
            raise ValueError("Error reading CARRIERS database at %s"%carrpath)


        self.read_carriers(data_carr)

        data_carr.close()

    def read_carriers(self,database):
        """
        Read output carriers
        """
        self.diff_carriers = database.variables['carriers_values'][:,1]    
        self.hole_carriers = database.variables['carriers_values'][:,2]
        self.elec_carriers = database.variables['carriers_values'][:,3]
        #Ratio between carrier difference and average
        self.ratio_carriers = self.diff_carriers/(0.5*(self.hole_carriers+self.elec_carriers))
    
    def __str__(self):
        s = ""
        return s

