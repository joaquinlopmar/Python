# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 08:40:09 2023

@author: jlm55b
"""

import os
import shutil as sh

Ruta = os.getcwd()
Archivos = os.listdir()
print(Archivos)

Ficheros = []

for Archivo in Archivos:
    if os.path.isfile(Archivo):
        Ficheros.append(Archivo)
       
for Fichero in Ficheros:
    Directorio = Fichero[1:4]
    if not(os.path.isdir(Directorio)):
        os.mkdir(Directorio)
    if not(os.path.isfile(Directorio + '//' + Fichero)):
        sh.copy(Fichero, Directorio + '//' + Fichero) 

print()
print(Ficheros)
print()
print(os.listdir())