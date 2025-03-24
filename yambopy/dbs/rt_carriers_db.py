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

    def __init__(self,folder='.',calc='SAVE',carriersdb='ndb.RT_carriers'):
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
        Read carriers database
        """
    
    def __str__(self):
        s = ""
        return s

