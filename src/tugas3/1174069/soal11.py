# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:56:34 2019

@author: FannyShafira
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
isidata = sf.records() #sf.records maksudnya berisikan data dbf
print(isidata[0]) #untuk mencetak isi data
print(isidata[0][0]) #untuk print array multidimensi

# In[]