# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:32:54 2019

@author: ADVENT
"""
import shapefile # Meng-import library shapefile
w = shapefile.Writer('3', shapeType=1)  # untuk Membuat penggambar pada shapefile yang nantinya akan di namakan nomor3 dan bentuknya itu adalah shapetype 1 yaitu point (titik)
 
w.field("kolom1","C")  # untuk Membuat table dengan kolom pertama
w.field("kolom2","C")  # untuk Membuat table dengan kolom kedua
 
w.record("ngek","satu") #  untuk Mengisi table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2
w.record("ngok","dua")  #  untuk Mengisi table yaitu ngok adalah isi pada kolom1 dan satu adalah isi pada kolom2
 
w.point(1,1) #  point (titik) pada koordinat x,y yaitu 1,1
w.point(2,2) #  point (titik) pada koordinat x,y yaitu 2,2

w.close() # Menutup (writer) karena kita sudah beres menggambar yang kita perlukan